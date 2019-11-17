import pytesseract
from PIL import Image
import datefinder
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


sno = 1
file = ["4.jpg","PF.jpeg", "pf.jpg", "0358c6c3.jpeg","b666ee43.jpeg","unnamed.jpg" ]

for x in file:
        print("S.NO :",sno, "Starting...")
        im = Image.open(x)

        text = pytesseract.image_to_string(im, lang = 'eng')
        my_list = []
        #print(text)
        if(re.findall(r'\d{2}/\d\d\/\d{2}', text)!=""):
            allmatches1=  re.findall(r'\d{2}/\d\d\/\d{2}', text)
            my_list.append(allmatches1)
            #print(allmatches1)
        if(re.findall(r'\d{2}/\w{3}\/\d{2}', text)!=""):
            allmatches2 = re.findall(r'\d{2}/\w{3}\/\d{2}', text)
            my_list.append(allmatches2)
           # print(allmatches2)
        if(re.findall(r'\d{2}/\d\d\/\d{4}', text)!=""):
            allmatches3 = re.findall(r'\d{2}/\d\d\/\d{4}', text)
            my_list.append(allmatches3)
            #print(allmatches3)
#
        if (re.findall(r'\d{2}-\d\d\-\d{4}', text)!=""):
            allmatches4 = re.findall(r'\d{2}-\d\d\-\d{4}', text)
            my_list.append(allmatches4)
            #print(allmatches4)
        if (re.findall(r'\d{2}-\d\d\-\d{2}', text)!=""):
            allmatches5 = re.findall(r'\d{2}-\d\d\-\d{2}', text)
            my_list.append(allmatches5)
            #print(allmatches5)
        if (re.findall(r'\d{2}-\w{3}-\d{2}', text)!=""):
            allmatches6 = re.findall(r'\d{2}-\w{3}-\d{2}', text)
            my_list.append(allmatches6)
            #print(allmatches6)
        if (re.findall(r'\d{2}-\w{3}-\d{4}', text)!=""):
            allmatches7 = re.findall(r'\d{2}-\w{3}-\d{4}', text)
            my_list.append(allmatches7)
            #print(allmatches7)
#
        if (re.findall(r'\d{2}\s\w{3}\\s\d{2}', text)!=""):
            allmatches8 = re.findall(r'\d{2}\s\w{3}\\s\d{2}', text)
            my_list.append(allmatches8)
            #print(allmatches8)
        if (re.findall(r'\d{2}\s\w{3}\s\d{4}', text)!=""):
            allmatches9 = re.findall(r'\d{2}\s\w{3}\s\d{4}', text)
            #my_list.append(allmatches9)
            print(allmatches9)
        if (re.findall(r'\d{2}\s\d{2}\s\d{2}', text)!=""):
            allmatches10 = re.findall(r'\d{2}\s\d{2}\s\d{2}', text)
            my_list.append(allmatches10)
            #print(allmatches10)
        if (re.findall(r'\d{2}\s\d{2}\s\d{4}', text)!=""):
            allmatches11 = re.findall(r'\d{2}\s\d{2}\s\d{4}', text)
            my_list.append(allmatches11)
            #print(allmatches11)
        else:
            print("NULL")
        print(my_list)
        #
        #matches = datefinder.find_dates(text)

        #for match in matches:
            #    print(match)

        print("-----------------------------------")
        sno=sno+1
        my_list = []