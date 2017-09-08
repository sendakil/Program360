
import docx
import sys
from docx.shape import InlineShape, InlineShapes
from docx.enum.shape import WD_INLINE_SHAPE
from docx import Document

inline_shapes_count={'no_of_pictures':0,'no_of_linkedpictures':0,'no_of_charts':0,'no_of_smartarts':0,'no_of_notimplemented':0}

file_name= "C:\\Program360\\Sample\\MySample01.docx"
word_file=open(file_name,'rb+')
word_document=Document(word_file)

word_shapes = word_document.inline_shapes
word_shapes_count=0

for word_shape in word_shapes:
    word_shapes_count+=1
    if word_shape.type==WD_INLINE_SHAPE.PICTURE:
       inline_shapes_count['no_of_pictures']+=1
                  
    elif word_shape.type==WD_INLINE_SHAPE.LINKED_PICTURE:
        inline_shapes_count['no_of_linkedpictures']+=1
    elif word_shape.type==WD_INLINE_SHAPE.CHART:
       inline_shapes_count['no_of_charts'] +=1
    elif word_shape.type==WD_INLINE_SHAPE.SMART_ART:
       inline_shapes_count['no_of_smartarts'] +=1
    elif word_shape.type==WD_INLINE_SHAPE.NOT_IMPLEMENTED:
        inline_shapes_count['no_of_notimplemented'] +=1
   

print(inline_shapes_count)





        




    
print (word_shapes_count)

#def getText(filename):
#    doc = docx.Document(filename)
#    fullText = []
#    for para in doc.paragraphs:
#        fullText.append(para.text)
#    return '\n'.join(fullText)




#file01= "C:\\Program360\\Sample\\MySample01.docx"

#text1 =getText(file01)
#doc1 = Document(file01)

#tables = doc1.tables

#for table in tables:
#    for row in table.rows:
#        for cell in row.cells:
#            for paragraph in cell.paragraphs:
#                print(paragraph.text)

#print(text1)


#inline_shapes = doc1.body.InlineShapes
#for inline_shape in inline_shapes:
#    print(inline_shape.type)









