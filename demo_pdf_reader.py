from pypdf import PdfReader

reader = PdfReader('file-sample_150kB.pdf')
print(len(reader.pages)) 
page = reader.pages[1]    
page.extract_text()

data_per_page = {}

for page_num in range(len(reader.pages)):
    current_page = reader.pages[page_num]
    data_per_page[page_num+1] = current_page.extract_text()

print("---->This is data for the pdf", data_per_page)