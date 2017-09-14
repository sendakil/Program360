from endec import EnDec
from etl.pdf.pdf_reader import PdfReader 
from etl.face.face_reader import HumanFaceDetector
from etl.doc.doc_reader import DocReader



# pdf reader 

config = dict(DRIVER='{ODBC Driver 11 for SQL Server}',
                server=   'RAJASENTHIL\SQLEXPRESS',
              port=      1433,                   
              database= 'Taxi',
              username= 'sa',
              password= '')

input_pdf_file="C:\\Program360\\Sample\\MySample01.pdf"
output_file="C:\\Program360\\Sample\\MySample01.csv"
output_json_file="C:\\Program360\\Sample\\MySample01.json"
doc_file_name= "C:\\Program360\\Sample\\MySample01.docx"
image_path="C:\\Program360\\Sample\\mp3.png"
cascade_path="C:\\Program360\\Sample\\haarcascade_frontface_default.xml"
detect=1

pdf01=PdfReader(input_pdf_file,1)
print(pdf01.layout_objects_count)

#pdf01.saveTextFile(output_file)
#pdf01.readTextFile(output_file)


#conn_str='DRIVER={SQL Server Native Client 11.0};SERVER='+config['server']+ ';DATABASE='+config['database']+';UID='+config['username']+';PWD='+ config['password']
#pdf01.saveMsSql(conn_str)
#pdf01.readMsSql(conn_str)

#pdf01.saveJSON(output_json_file)
#pdf01.readJSON(output_json_file)

### pdf reader 

#Face Reader 


#face01=HumanFaceDetector(image_path,cascade_path,detect)
#print(face01.getAuthor())
#print(face01.getVersion())



##Document Reader

doc01=DocReader(doc_file_name,1)
print(doc01.inline_shapes_count)


  