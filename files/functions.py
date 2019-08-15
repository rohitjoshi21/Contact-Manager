import re
import vobject
from pandas import DataFrame
import os

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
'''


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
    email = [person.email for person in cons]
    address = [person.address for person in cons]
    #create a pandas dataframe of contacts
    df = DataFrame({'Name':name,'Phone':phone,'Email':email,'Address':address}) 
    df.style.set_properties(**{'text-align': 'left'})
    return df

def getNewContact():
    infs = {}
    infs['fn'] = name = input('\nEnter the name:- ')
    infs['tel'] = input('Enter the phone number:- ')
    infs['email'] = input('Enter the email:- ')
    infs['adr'] = input('Enter your address:- ')
    return infs


def searchContactByAttr(cons,query,attribute):
    '''Simple searching
    cons = list of contact objecta
    query = keyword to search
    attribute = field to search'''

    #Not an efficient algorithm
    
    i = None
    for index,contact in enumerate(cons):
        if contact.getValue(attribute) == query:
            i = index
            break
        
    return i
        
def searchContact(cons,q):
    '''
    Search contacts (cons) with the given query (q)
    And return index of the found contact'''
    
    index = None
    
    #Checking whether it is phone number or contact name
    if q.isdigit and 9<=len(q)<=10:
        #search the number in phone of contacts and return the index
        
        index = searchContactByAttr(cons,q,'phone')
        

    elif type(q) == str:
        #search the name in contacts and return the index

        index = searchContactByAttr(cons,q,'name')

    return index

def saveContacts(cons,filename):
    sortContacts(cons)

    #Saving contacts in new vcard file
    outputfile = open(filename,'w')
    for contact in cons:
        f = objToVcard(contact) #returns vcard text from dictionary given
        outputfile.write(f)

    outputfile.close()
                      
if __name__ == '__main__':
    c = getSeparateVcards(a)
    print(vcardToDict(c[-1]))


