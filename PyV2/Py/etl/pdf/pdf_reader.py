
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



class PdfReader(object):
   

    no_of_objects=0
    __author="Rajagopal senthil kumar, sendakil@yahoo.com"
    __version="01.00.00"


    def __init__(self,file_name="",extract_yes=0):
       PdfReader.no_of_objects+=1 
       self.pdf_resource=PDFResourceManager()
       self._pdf_params=LAParams()
       self.pdf_device=PDFPageAggregator(self.pdf_resource,laparams=self._pdf_params)
       self.pdf_interpreter=PDFPageInterpreter(self.pdf_resource,self.pdf_device)
       self.layout_objects_count={'no_of_images':0,'no_of_figures':0,'no_of_rect':0,'no_of_text':0,'no_of_othertext':0}
       self.extracted_texts=[]
       if file_name!="":
           self.file_name=file_name
           self.pdf_file =open(file_name,'rb')
           if extract_yes!=0:
               self.countLayoutObjects(extract_yes)

    def getVersion(self):
        return self.__version

    def getAuthor(self):
        return self.__author
      
     
    def loadPDFdocument(self,file_name):
        self.file_name=file_name
        self.pdf_file =open(file_name,'rb')
            
      
    def countLayoutObjects(self,extract_yes=0):
        
        for pdf_page in PDFPage.get_pages(self.pdf_file):
            self.pdf_interpreter.process_page(pdf_page)
            pdf_layout=self.pdf_device.get_result()
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


