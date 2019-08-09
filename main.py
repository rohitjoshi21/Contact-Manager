from person import Person
from functions import *



VCF_FILE_NAME = 'Modified sample.vcf'


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
'''

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
    choice = get_int_input(max = 5)

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
        data = inpt('Enter the new {}? '.format(fieldname))

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
        print(df)
        
    elif choice == 5:
        #Exiting
        exit = True








sortContacts(CONTACTS)

#Saving contacts in new vcard file
outputfile = open('Modified '+VCF_FILE_NAME,'w')
for contact in CONTACTS:
    f = objToVcard(contact) #returns vcard text from dictionary given
    outputfile.write(f)

outputfile.close()
