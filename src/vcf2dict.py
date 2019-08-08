#!/usr/bin/python3

import re
from vobject import *

#Location of vcf file
vcf_file = 'test.vcf'

main_data = {}

'''
 data_needed is compulsory argument to run the function 'store_if_exists'.
 This function stores the data likes email,photo etc if available otherwise return Null.

 To add different data in dictionary just add key value pair in the dictionary below,
 key must be appropriate with vobject whereas value can be any variable.
'''

data_needed = {'fn':'Name','tel':'Telephone','email':'Email','photo':'Photo'}

# ----VCF file to dictionary----

def vcf2dict(vcf_file):

    with open(vcf_file,'r') as f_in:
        raw_data = f_in.read()

    def store_if_exists(data_needed):
        temp_data = {}

        for key in data_needed:
                # main_data[data.contents['fn'][0].value] will be a dictionary if the key is unique
                if type(main_data[data.contents['fn'][0].value]) == dict:
                    try:
                        # if data contains double value for eg more than one email than make lists
                        if len(data.contents[key]) >= 2:
                            main_data[data.contents['fn'][0].value].update({data_needed[key]:[] })

                            for j in range(len(data.contents[key])):
                                main_data[data.contents['fn'][0].value][data_needed[key]].append(data.contents[key][j].value)
                        # if data contains only one value , dont make list
                        else:
                            main_data[data.contents['fn'][0].value].update({data_needed[key]:data.contents[key][0].value })

                    except KeyError:
                        main_data[data.contents['fn'][0].value].update({data_needed[key]: 'Null'})

                # main_data[data.contents['fn'][0].value] will be a list if the key is not unique
                elif  type(main_data[data.contents['fn'][0].value]) == list:
                    try:
                        if len(data.contents[key]) >= 2: # If data contain more than one value
                            temp_data.update({data_needed[key]:[] })

                            for j in range(len(data.contents[key])):
                                temp_data[data_needed[key]].append(data.contents[key][j].value)
                        else:
                            temp_data.update({data_needed[key]:data.contents[key][0].value }) # If data contain only one value
                    except KeyError:
                        temp_data.update({data_needed[key]: 'Null' }) # If data not found
        # Append temp_data inside the main_data ... For duplicate key
        try:
            main_data[data.contents['fn'][0].value].append(temp_data)
        except AttributeError:
            pass


    # Get separate vcard
    pattern = 'BEGIN:VCARD.*?END:VCARD'  #regex for matching each contacts
    contacts = re.findall(pattern,raw_data,re.DOTALL) #searching above pattern in given datas

    # Passing the splitted data into vobject
    for i in range(len(contacts)):
        # vcard to vobject
        data = readOne(contacts[i])

        # Creating Main key for the dictionary main_data,
        # main_data.update({ data.contents[x][0].value : {} })
        # Replace x with any var which you want as the main key of nested dictionary
        try:
            # search if the key is unique or not.
            name_key = data.contents['fn'][0].value
            # If key is not unique make a list
            if name_key  in main_data:
                main_data.update({ name_key : [] })

            # Else make a dictionary insted of list
            else:
                main_data.update({ name_key : {} })

        except KeyError:
            continue

    # Fill the empty list or dictionary with data
    for k in range(len(contacts)):
        data = readOne(contacts[k])
        try:
            store_if_exists(data_needed)
        except KeyError:
            pass

    print(main_data)


vcf2dict(vcf_file)
