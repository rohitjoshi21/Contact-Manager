#!/usr/bin/python3

from files.person import Person
from files.functions import *
import os

root_dir = 'files'
VCF_FILE_NAME = os.path.join(root_dir,'sample2.vcf')


attributesListMessage = \
'''
What do you want to edit? \n
1. Name
2. Phone
3. Email
4. Address
5. Org
'''

attributes = ['name','phone','email','address','org']

optionsListMessage = \
'''
What do you want to do? \n
1. Add new contact
2. Edit existing contact
3. Delete a contact
4. Display contacts
5. Save and exit
6. Create New File
'''
maxOptions = 6
#Location of vcf file


contents = open(VCF_FILE_NAME).read()
vcards = getSeparateVcards(contents) #breaks whole vcard file into seperate vcards


CONTACTS = []
for vcard in vcards:
    inf = vcardToDict(vcard)  #return dict with all available informations
    new_contact = Person(inf) #creates a new person object for each contact
    CONTACTS.append(new_contact) #Add this object in a list


#in_place contacts sorting on the basis of attribute name
sortContacts(CONTACTS)

#Program execution part
exit = False
while not exit:
    
    print(optionsListMessage)
    
    #Get a integer number to choose a option
    choice = get_int_input(max = maxOptions)

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

        #getting name of the chosen field
        fieldname = attributes[choice-1]

        #asking for new value of the chosen field
        data = input('Enter the new {}? '.format(fieldname))

        #saving the new value in contacts list
        CONTACTS.setValue(fieldname,data)        
    
    elif choice == 3:
        #Deleting a contact

        query = input('Enter name or number of the contacts you want to delete:- ')
        index = searchContact(CONTACTS,query) #getting index of the required contact in CONTACTS list.
        if not index:
            print('No contact found')
            continue

        #deleting the chosen contact
        del CONTACTS[index]
        
    elif choice == 4:
        #Show contacts in a table
        df = contactsTable(CONTACTS)
        print('*'*80)
        print(df)
        print('*'*80)
        
    elif choice == 5:
        #Exiting
        saveContacts(CONTACTS,VCF_FILE_NAME)
        exit = True

    elif choice == 6:
        #Creating new vcf file to store new contacts

        saveContacts(CONTACTS,VCF_FILE_NAME)
        CONTACTS = []
        VCF_FILE_NAME = os.path.join(root_dir,'NewContact.vcf')
        
    
        
print('\n\nThank you for using this! Keep supporting us!')


