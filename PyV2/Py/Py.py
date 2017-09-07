
from etl.pdf.pdf_reader import PdfReader 
from etl.face.face_reader import HumanFaceDetector

# pdf reader 
config = dict(DRIVER='{ODBC Driver 11 for SQL Server}',
                server=   'RAJASENTHIL\SQLEXPRESS',
              port=      1433,                   
              database= 'Taxi',
              username= 'sa',
              password= 'shambhavvi')

input_pdf_file="C:\\Program360\\Sample\\MySample01.pdf"
output_file="C:\\Program360\\Sample\\MySample01.csv"
output_json_file="C:\\Program360\\Sample\\MySample01.json"
conn_str='DRIVER={SQL Server Native Client 11.0};SERVER='+config['server']+ ';DATABASE='+config['database']+';UID='+config['username']+';PWD='+ config['password']

pdf01=PdfReader(input_pdf_file,1)
print(pdf01.getAuthor())
print(pdf01.getVersion())
#pdf01.countLayoutObjects(1)
print(pdf01.extracted_texts)
print(pdf01.layout_objects_count)

pdf01.saveTextFile(output_file)
#pdf01.readTextFile(output_file)
#pdf01.saveMsSql(conn_str)
#pdf01.readMsSql(conn_str)
pdf01.saveJSON(output_json_file)
#pdf01.readJSON(output_json_file)

### pdf reader 

#Face Reader 

image_path="C:\\Program360\\Sample\\mp3.png"
cascade_path="C:\\Program360\\Sample\\haarcascade_frontface_default.xml"
detect=1

face01=HumanFaceDetector(image_path,cascade_path,detect)
print(face01.getAuthor())
print(face01.getVersion())



