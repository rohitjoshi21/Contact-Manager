from files.person import Person
from files.functions import *
import os

menubar = \
'''
1. Create New File
2. Open File
3. Add New Contact
4. Edit a contact
5. Delete a contact
6. Update contacts
7. Save progress
8. Exit
'''

#Getting no of options in menubar
maxOptions = len(menubar.split('\n'))

attributesListMessage = \
'''
What do you want to edit?

1. Name
2. Phone
3. Email
4. Address
5. Org
'''

attributes = ['name','phone','email','address','org']

current_file = None
CONTACTS = []
table = None
#Program Execution
exit = False
while not exit:

    #Screen texts
    cf = ' ' if current_file == None else current_file
    print('{:^80}\n'.format('Contact Editor 1.0 '+cf))
    print
    print('*'*80)
    print('{:^80}'.format('Contacts Table'))
    try:
        c = len(table.index)
    except:
        print('{:^80}'.format('No Table Found.'))
        print('{:^80}'.format("Enter '6' to update contacts in table"))
    else:
        print('%d contacts found'%c,'\n')
        print(table)
    print('*'*80)
    print(menubar)

    print('Choose an option from above menus (1-{}) ?'.format(maxOptions))
    choice = get_int_input(max = maxOptions)

    if choice == 1:
        print('Enter name of the new file?')
        c = input()
        if current_file:
           saveContacts(CONTACTS,current_file)
        current_file = c
        table = None
        CONTACTS = []
       
    elif choice == 2:
        print('Enter path of the file relative to this program?')
        c = input()
        
        try:
            #check whether c exits or not
            contents = open(c).read()   
        except:
            print('There is no file named ',c)
            
        else:
            if current_file != None:
                saveContacts(CONTACTS,current_file)
            current_file = c
            contents = open(current_file).read()
            #breaks whole vcard file into seperate vcards
            vcards = getSeparateVcards(contents) 

            CONTACTS = []
            for vcard in vcards:
                inf = vcardToDict(vcard)  #return dict with all available informations
                new_contact = Person(inf) #creates a new person object for each contact
                CONTACTS.append(new_contact) #Add this object in a list


            #in_place contacts sorting on the basis of attribute name
            sortContacts(CONTACTS)
            

    elif choice == 3:
        #Adding new contacts

        #Asking for the information of new contact
        newcont = getNewContact()
        #Adding new contact in contact list
        CONTACTS.append(Person(newcont))

    elif choice == 4:
        #Editing exiting contact

        query = input('Enter name or number of the contacts you want to edit:- ')
        index = searchContact(CONTACTS,query) #getting index of the required contact in CONTACTS list.
        if not index:
            print('No contact found')
            continue
        print('Contact found: Name:- {} Phone:- {}'.format(CONTACTS[index].name,CONTACTS[index].phone))
        #Showing options to edit a contact
        print(attributesListMessage)

        #getting a option number which user wants to edit
        choice = get_int_input()

        #getting name of the chosen field
        fieldname = attributes[choice-1]

        #asking for new value of the chosen field
        data = input('Enter the new {}? '.format(fieldname))

        #saving the new value in contacts list
        CONTACTS[index].setValue(fieldname,data)        

    elif choice == 5:
        #Deleting a contact

        query = input('Enter name or number of the contacts you want to delete:- ')
        index = searchContact(CONTACTS,query) #getting index of the required contact in CONTACTS list.
        if not index:
            print('No contact found')
            continue
        print('Contact found: Name:- {} Phone:- {}'.format(CONTACTS[index].name,CONTACTS[index].phone))
        #deleting the chosen contact
        del CONTACTS[index]
        print('Contact Deleted Successfully')

    elif choice == 6:
        #Update the contacts in table
        sortContacts(CONTACTS)
        table = contactsTable(CONTACTS)

    elif choice == 7:
        saveContacts(CONTACTS,current_file)

    elif choice == 8:
        yesno = input('\nDo you want to save {} before closing? (Y/N)'.format(current_file))

        if yesno.lower() in ['yes','y','ok']:
            saveContacts(CONTACTS,current_file)
        exit = True
        
    
    os.system('clear')
