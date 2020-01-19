import os
import re
import textract


def extract(file_path):
    text = textract.process(file_path)
    return text.decode('utf-8')


def clean_extract(mystring):
    return re.sub('[^A-Za-z0-9]+', '', mystring)


if __name__ == '__main__':
    for item in os.listdir('/Users/vikranth/Documents'):
        pass
    # pdf_data = extract_pdf('/Users/vikranth/Downloads/output-1.pdf')
    # clean_extract(pdf_data)
    print(extract(''))
