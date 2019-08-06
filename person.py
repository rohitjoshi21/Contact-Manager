class Person:
    def __init__(self,datas):
        self.set_values(datas)

    def set_values(self,datas):
        """ Sets values of required fields

        It takes the data from dictionary and store them as
        attribute of this object"""

        #These keys are replaced for convenience while writing codes
        replace_keys = {'fn':'name','tel':'phone','adr':'address',}
        
        defaults = {"fn"    : None,
                    "tel"   : None,
                    "email" : None,
                    "adr"   : None,
                    "org"   : None,
                    "photo" : None,}

        
                    
        for field in datas:
            if field in defaults:
                defaults[field] = datas[field]
            else:
                continue

               #raise KeyError("Person contains no field {}.".format(field))

        for key in replace_keys:
            if key in defaults:
                defaults[replace_keys[key]] = defaults.pop(key)
                         
        self.__dict__.update(defaults)

    
    
