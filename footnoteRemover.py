#! python3
# footnoteRemover.py - Removes footnotes from word documents.

import os, docx

os.chdir('C:\\Reader')

doc = docx.Document('') #input doc name
cleanDoc = docx.Document()

# search through every paragraph, remove ones that start with a #
for i in range(len(doc.paragraphs)):
    if doc.paragraphs[i].text != '':
        if doc.paragraphs[i].text[0].isdigit():
            #print(doc.paragraphs[i].text)
            continue
    cleanDoc.add_paragraph(doc.paragraphs[i].text)

cleanDoc.save('cleanedDoc.docx')
