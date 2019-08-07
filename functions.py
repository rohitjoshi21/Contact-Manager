import re
import vobject
import pandas as pd

a =\
'''BEGIN:VCARD
VERSION:3.0
N:-Achham;Bhaskar;Saud;;
FN:Bhaskar -Achham
NOTE:
TEL;TYPE=CELL;TYPE=pref;TYPE=VOICE:9741062727
PRODID:-//Apple Inc.//iCloud Web Address Book 1912B18//EN
REV:2019-07-24T09:44:46Z
END:VCARD
BEGIN:VCARD
VERSION:3.0
N:Gump;Forrest;;Mr.;
FN:Forrest Gump
ORG:Bubba Gump Shrimp Co.
TITLE:Shrimp Man
PHOTO;VALUE=URI;TYPE=GIF:;http://www.example.com/dir_photos/my_photo.gif
TEL;TYPE=WORK,VOICE:(111) 555-1212
TEL;TYPE=HOME,VOICE:(404) 555-1212
ADR;TYPE=WORK,PREF:;;100 KTm
LABEL;TYPE=WORK,PREF:100 Ktm
ADR;TYPE=HOME:;;42 Plantation jpt
LABEL;TYPE=HOME:42 Plantation jpt
EMAIL:forrestgump@example.com
REV:2008-04-24T19:52:43Z
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:A-Z-Badeda-5Bada-10-BGM-Bajura-7-Vot-DV-FV-PBM-CCM-DCM-CM-VMCM-WCM-INCH-
VMCP/C-PM-MIN-MP-VML-DL-WL-VL-TL-BL-HL-HH-MOV-NCV-UMLV-OV-NV-Ma-Fe-Da-OC-AP
A-SF-GOE-NGOE-POE-BOE-UP-NC
N:;A-Z-Badeda-5Bada-10-BGM-Bajura-7-Vot-DV-FV-PBM-CCM-DCM-CM-VMCM-WCM-INCH-
VMCP/C-PM-MIN-MP-VML-DL-WL-VL-TL-BL-HL-HH-MOV-NCV-UMLV-OV-NV-Ma-Fe-Da-OC-AP
A-SF-GOE-NGOE-POE-BOE-UP-NC;;;
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:A-Z-Bahungaun-8Bada-10-BGM-Bajura-7-Vot-DV-FV-PBM-CCM-DCM-CM-VMCM-WCM-IN
CH-VMCP/C-PM-MIN-MP-VML-DL-WL-VL-TL-BL-HL-HH-MOV-NCV-UMLV-OV-NV-Ma-Fe-Da-OC
APA-SF-GOE-NGOE-POE-BOE-UP-NCe
N:;A-Z-Bahungaun-8Bada-10-BGM-Bajura-7-Vot-DV-FV-PBM-CCM-DCM-CM-VMCM-WCM-IN
CH-VMCP/C-PM-MIN-MP-VML-DL-WL-VL-TL-BL-HL-HH-MOV-NCV-UMLV-OV-NV-Ma-Fe-Da-OC
-APA-SF-GOE-NGOE-POE-BOE-UP-NCe;;;
END:VCARD'''


def getSeparateVcards(dump):
    pattern = 'BEGIN:VCARD.*?END:VCARD'  #regex for matching each contacts
    match = re.findall(pattern,dump,re.DOTALL) #searching above pattern in given datas
    return match   

    
def vcardToDict(vcard_raw,required = ['fn','tel','email','photo','adr','org']):
    inf = {}
    data = vobject.readOne(vcard_raw) #converting vcard in vobject

    for r in required:
        if r in data.contents.keys():
            try:
                inf[r] = data.contents[r][0].value #adding required field in our data
            except:
                pass
        else:
            inf[r] = None

    return inf

def dictToVcard(dicts):
    return None

def sortContacts(cons):
    cons.sort(key=lambda x: x.name.lower()) 


def contactsTable(cons):
    name = [person.name for person in cons]
    phone = [person.phone for person in cons]
    df = pd.DataFrame({'name':name,'phone':phone}) #create a pandas dataframe of contacts
    df.style.set_properties(**{'text-align': 'left'})
    return df

def getNewContact():
    infs = {}
    infs['fn'] = name = input('\n Enter the name:- ')
    infs['tel'] = input('Enter the phone number:- ')
    infs['email'] = input('Enter the email:- ')
    return infs

def searchContact(cons,q):
    index = None
    if q.isdigit and 9<=len(q)<=10:
        #search the number in phone of contacts and return the index
        pass

    else:
        #search the name in contacts and return the index

    return index
    
if __name__ == '__main__':
    c = getSeparateVcards(a)
    print(vcardToDict(c[1]))


