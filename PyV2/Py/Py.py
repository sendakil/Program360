
from etl.pdf.pdf_reader import PdfReader 

pdf01=PdfReader("c:\\Me\\Python\\MySample01.pdf",1)
print(pdf01.getAuthor())
print(pdf01.getVersion())
pdf01.countLayoutObjects(1)
print(pdf01.extracted_texts)
print(pdf01.layout_objects_count)