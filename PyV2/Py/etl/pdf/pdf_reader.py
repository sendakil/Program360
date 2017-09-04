
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    Author: Rajagopal Senthil Kumar
    Created Date:  01-Sep-2017
    Modified Date: 01-Sep-2017
    Purpose: Module to read pdf content and identify texts, images, figures, etc.,

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.converter import  PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams,LTTextBoxHorizontal,LTImage,LTFigure,LTRect,LTTextBox,LTLine
import io
import pyodbc
import json


class PdfReader(object):
   

    no_of_objects=0
    __author="Rajagopal senthil kumar, sendakil@yahoo.com"
    __version="01.00.00"


    def __init__(self,file_name="",extract_yes=0):
       PdfReader.no_of_objects+=1 
       self._pdf_resource=PDFResourceManager()
       self._pdf_params=LAParams()
       self._pdf_device=PDFPageAggregator(self._pdf_resource,laparams=self._pdf_params)
       self._pdf_interpreter=PDFPageInterpreter(self._pdf_resource,self._pdf_device)
       self.layout_objects_count={'no_of_images':0,'no_of_figures':0,'no_of_rect':0,'no_of_text':0,'no_of_othertext':0}
       self.extracted_texts=[]
       if file_name!="":
           self.loadPDFdocument(file_name)
           if extract_yes!=0:
               self.countLayoutObjects(extract_yes)

    def getVersion(self):
        return self.__version

    def getAuthor(self):
        return self.__author
      
     
    def loadPDFdocument(self,file_name):
        try:
            self.file_name=file_name
            self.pdf_document =open(file_name,'rb')
        except IOError:
            print("Error: Can\'t file or read data")
        
               
      
    def countLayoutObjects(self,extract_yes=0):
        
        for pdf_page in PDFPage.get_pages(self.pdf_document):
            self._pdf_interpreter.process_page(pdf_page)
            pdf_layout=self._pdf_device.get_result()
            for layout_element in pdf_layout:
                if isinstance(layout_element,LTFigure):
                    self.layout_objects_count['no_of_figures']+=1
                elif isinstance(layout_element,LTImage):
                    self.layout_objects_count['no_of_images']+=1
                elif isinstance(layout_element,LTRect):
                    self.layout_objects_count['no_of_rect']+=1
                elif isinstance(layout_element,LTLine):
                    self.layout_objects_count['no_of_line']+=1
                elif isinstance(layout_element,LTTextBox):
                    self.layout_objects_count['no_of_text']+=1
                    if extract_yes!=0:
                       self.extracted_texts.append(layout_element.get_text())  
                else:
                    self.layout_objects_count['no_of_othertext']+=1

    def saveTextFile(self,file_name,col_delimiter=","):
        try:
            txt_file=open(file_name,"w+")
            txt_file.write("pdf_file,Seq,Content\n")
            i=1
            for extracted_text in self.extracted_texts:
                txt_cleaned=(extracted_text.strip()).replace("\n","|")
                txt_line=self.file_name+","+str(i)+col_delimiter+txt_cleaned+'\n'
                txt_file.write(txt_line)
                i+=1
        except IOError:
              print("Error: Can\'t file or read data")


    def readTextFile(self,file_name):
        try:
            txt_file=open(file_name,"r+")
            file_content=txt_file.readlines()
            for file_line in file_content:
                print(file_line)
                
        except IOError:
              print("Error: Can\'t file or read data")



    def saveMsSql(self,conn_str):
        try:
         conn =pyodbc.connect(conn_str)
         record_set=conn.cursor()
         insert_sql_str= "INSERT INTO dbo.pdf_extract(file_name, seq, content) values (?,?,?)"
         i=1
         for extracted_text in self.extracted_texts:
                txt_cleaned=(extracted_text.strip()).replace("\n","|")
                record_set.execute(insert_sql_str,self.file_name,i,txt_cleaned)
                i+=1
         record_set.commit()
         record_set.close()

        except Exception:
             print("Error: MS Sql connection ")



    def readMsSql(self,conn_str):
        try:
         conn =pyodbc.connect(conn_str)
         record_set=conn.cursor()
         select_sql_str= "select file_name, seq, content from dbo.pdf_extract"
         record_set.execute(select_sql_str)
         
         for row in record_set.fetchall():
             print(row)

        except Exception:
             print("Error: MS Sql connection ")



    def saveJSON(self,file_name):
        try:
            json_dataset={}
            json_dataset['pdf_recordset']=[]
         
            i=1
            for extracted_text in self.extracted_texts:
                txt_cleaned=(extracted_text.strip()).replace("\n","|")
                tx_json_format={'file_name':self.file_name,'i':i,'Content':txt_cleaned}
                json_dataset['pdf_recordset'].append(tx_json_format)
                i+=1
                
            json_file=open(file_name,"w+")
            json.dump(json_dataset,json_file)

        except IOError:
              print("Error: Can\'t file or read data")


    def readJSON(self,file_name):
        try:
 
                
            json_file=open(file_name,"r+")
            json_dataset=json.load(json_file)

            for json_record in json_dataset['pdf_recordset']:
                print('File Name:' ,json_record['file_name'])
                print('Content:', json_record['Content'])
                
        except IOError:
              print("Error: Can\'t file or read data")


   