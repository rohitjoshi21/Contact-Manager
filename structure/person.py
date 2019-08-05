class Person:
    def __init__(self,datas):
        self.set_values(datas)

    def set_values(self,datas):
        """ Sets values of required fields

        It takes the data from dictionary and store them as
        attribute of this object"""
        
        defaults = {"name"  : None,
                    "tel"   : None,
                    "email" : None,
                    "adr"   : None}
                    
        for field in information:
            if field in defaults:
                defaults[field] = datas[field]
            else:
                raise KeyError("Person contains no field {}.".format(field))
        self.__dict__.update(defaults)

    
    
