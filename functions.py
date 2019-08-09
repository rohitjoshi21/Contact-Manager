import re
import vobject
import pandas as pd

#Sample Data
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
N:;A-Z-Bahungaun-8Bada-10-BGM-Bajura-7-Vot-DV-FV-PBM-CCM-DCM-CM-VMCM-WCM-IN;;;
ADDRESS: Kathmandu, Nepal
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
            inf[r] = str(data.contents[r][0].value).replace('\n','') #adding required field in our data
        else:
            inf[r] = None

    return inf

def get_int_input(min=1,max=4):
    '''Return integer input within min and max range'''
    op = input()
    if not op.isdigit() or int(op) < min or int(op)> max:
        print('Invalid Input. Enter again ? \n')
        op =  get_input()
    return int(op)

def objToVcard(obj):
    replace = {'name':'fn','email':'email','phone':'tel','address':'adr','photo':'photo','org':'org'}
    
    '''Returns a vcard format text for a single contact object having
    the required information
    contactObj must contains following attributes:-
    name,address,phone,org,.....'''
    person = obj.__dict__
    person = {replace[key]: value for key,value in person.items() if value != None}
    print(person)
    vcard = vobject.readOne('\n'.join([f'{k}:{v}' for k, v in person.items()]))
    vcard.name = 'VCARD'
    vcard.useBegin = True
    return vcard.serialize()


def sortContacts(cons):
    cons.sort(key=lambda x: x.name.lower()) 


def contactsTable(cons):
    '''Returns a pandas table of the contacts'''
    name = [person.name for person in cons]
    phone = [person.phone for person in cons]
    df = pd.DataFrame({'name':name,'phone':phone}) #create a pandas dataframe of contacts
    df.style.set_properties(**{'text-align': 'left'})
    return df

def getNewContact():
    infs = {}
    infs['fn'] = name = input('\nEnter the name:- ')
    infs['tel'] = input('Enter the phone number:- ')
    infs['email'] = input('Enter the email:- ')
    infs['adr'] = input('Enter your address:- ')
    return infs

def searchContact(cons,q):
    '''
    Search contacts (cons) with the given query (q)
    And return index of the found contact'''
    
    #Not Completed
    
    index = None
    
    #Checking whether it is phone number or contact name
    if q.isdigit and 9<=len(q)<=10:
        #search the number in phone of contacts and return the index
        pass

    else:
        pass
        #search the name in contacts and return the index

    return index
    
if __name__ == '__main__':
    c = getSeparateVcards(a)
    print(vcardToDict(c[-1]))


