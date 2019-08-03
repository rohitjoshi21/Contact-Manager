import re
from vobject import *

#Location of vcf file
vcf_file = 'your_vcf_file.vcf'

main_data = {}


'''
 data_needed is compulsory argument to run the function 'store_if_exists'.
 This function stores the data likes email,photo etc if available otherwise return Null.

 To add different data in dictionary just add key value pair in the dictionary below,
 key must be appropriate with vobject whereas value can be any variable.
'''

data_needed = {'tel':'Telephone','email':'Email','org':'Organization','adr':'Address'}


# ----VCF file to dictionary----

def vcf2dict(vcf_file):
    # Initail value to count duplicate name/key
    duplicate_key = {}


    with open(vcf_file,'r') as f_in:
        raw_data = f_in.read()


    # Store data if exists.
    def store_if_exists(data_needed):

        # Only for duplicate key, make a dictionary inside a list to store individual values of duplicate key
        if type(main_data[data.contents['fn'][0].value]) == list:
            for i in range(duplicate_key[data.contents['fn'][0].value]):
                try:
                    main_data[data.contents['fn'][0].value].append({})
                except KeyError:
                    continue

        for key in data_needed:

            # main_data[data.contents[x][0].value , replace x with the var which you want as a key of nested dict.
            try:
                # main_data[data.contents['fn'][0].value] will be a dictionary if the key is unique
                if type(main_data[data.contents['fn'][0].value]) == dict:
                    # if data contains double value for eg more than one email than making lists
                    if len(data.contents[key]) >= 2:
                        main_data[data.contents['fn'][0].value].update({data_needed[key]:[] })

                        for j in range(len(data.contents[key])):
                            main_data[data.contents['fn'][0].value][data_needed[key]].append(data.contents[key][j].value)
                    # if data contains only one value , dont make list
                    else:
                        main_data[data.contents['fn'][0].value].update({data_needed[key]:data.contents[key][0].value })

                # main_data[data.contents['fn'][0].value] will be a list if the key is not unique
                elif  type(main_data[data.contents['fn'][0].value]) == list:
                        pass

            except KeyError:
                try:
                    main_data[data.contents['fn'][0].value].update({data_needed[key]: 'Null'})
                except AttributeError:
                    main_data[data.contents['fn'][0].value].append({data_needed[key]: 'Null'})

    # --Splitting the datas--
    contacts = re.split('BEGIN',raw_data)

    # Removing the first element of lists because its blank
    contacts.pop(0)


    # Adding str 'BEGIN' infront of every elements because str 'BEGIN' was removed during splitting
    for i in range(len(contacts)):
        contacts[i] = 'BEGIN' + contacts[i]

    # --vobject--
    # Passing the splitted data into vobject


    for i in range(len(contacts)):
        data = readOne(contacts[i])

        # Creating Main key for the dictionary main_data,
        # main_data.update({ data.contents[x][0].value : {} })
        # Replace x with any var which you want as the main key of nested dictionary
        try:
            # search if the key is unique or not.

            # If key is not unique make a list
            name_key = data.contents['fn'][0].value
            if name_key  in main_data:

                main_data.update({ name_key : [] })
                #duplicate_key.update({data.contents['fn'][0].value :  a+1 })
                duplicate_key[name_key] += 1

            # Else make a dictionary insted of list
            else:
                main_data.update({ name_key : {} })


        except KeyError:
            continue

        # This function Store the data if available otherwise return Null
        store_if_exists(data_needed)

    print(main_data)


vcf2dict(vcf_file)
