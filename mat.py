import docx, json, string

lst = []

doc = docx.Document('плохие слова.docx')

for docpara in doc.paragraphs:
   lst = docpara.text.split(", ")


with open('cenz.json', 'w', encoding='utf-8') as jsn:
   json.dump(lst, jsn)


print(lst)
