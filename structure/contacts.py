from person import Person
from vcard import *

#Location of vcf file
VCF_FILE = 'Iphone.vcf'

contents = open(VCF_FILE).read()
vcards = getSeparateVcards(contents) #breaks vcard file into seperate contacts


CONTACTS = []
for vcard in vcards:
    inf = vcardToDict(vcard)  #return dict with all available informations
    new_contact = Person(inf) #creates a new person object for each contact
    CONTACTS.append(new)


CONTACTS = sortContacts(CONTACTS) #sorts contacts on the basis of name order


#performs anything here like adding new contact,editing
#
#
#
#
#

CONTACTS = sortContacts(CONTACTS) #sort contacts again at last

outputfile = open('Modified '+VCF_FILE,'w')
for contact in CONTACTS:
    f = dictToVcard(contact) #returns vcard text from dictionary given
    outputfile.write(f+'\n')

outputfile.close()
