from person import Person
from functions import *


attributesListMessage = \
'''
What do you want to edit? \n
1. Name
2. Phone
2. Email
3. Address
4. Org
'''

optionsListMessage = \
'''
What do you want to do? \n
1. Add new contact
2. Edit existing contact
3. Delete a contac
4. Save and exit
'''

#Location of vcf file
VCF_FILE = 'sample.vcf'

contents = open(VCF_FILE).read()
vcards = getSeparateVcards(contents) #breaks vcard file into seperate contacts


CONTACTS = []
for vcard in vcards:
    inf = vcardToDict(vcard)  #return dict with all available informations
    new_contact = Person(inf) #creates a new person object for each contact
    CONTACTS.append(new_contact) #Add this object in a list


#in_place contacts sorting on the basis of attribute name
sortContacts(CONTACTS) 

def get_int_input(min=1,max=4):
    '''Return integer input within min and max range'''
    op = input()
    if not op.isdigit() or int(op) < min or int(op)> max:
        print('Invalid Input. Enter again ? \n')
        op =  get_input()
    return int(op)

#Program execution part
exit = False
while not exit:
    
    print(optionsListMessage)
    choice = get_int_input()

    if choice == 1:
        #Adding new contacts

        #Asking for the information of new contact
        newcont = getNewContact()
        #Adding new contact in contact list
        CONTACTS.append(Person(newcont))

        
    elif choice == 2:
        #Editing exiting contact

        query = input('Enter name or number of the contacts you want to edit:- ')
        index = searchContact(CONTACTS,query) #getting index of the required contact in CONTACTS list.
        if not index:
            print('No contact found')
            continue

        #Showing options to edit a contact
        print(attributesListMessage)

        #getting a option number which user wants to edit
        choice = get_int_input()

        ###Not Completed
        

    
    elif choice == 3:
        #Deleting a contact
        pass
    
    elif choice == 4:
        #Exiting
        exit == True



##df = contactsTable(CONTACTS)
##print(df)





sortContacts(CONTACTS)

outputfile = open('Modified '+VCF_FILE,'w')
for contact in CONTACTS:
    f = dictToVcard(contact) #returns vcard text from dictionary given
    outputfile.write(f+'\n')

outputfile.close()
