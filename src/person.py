class Person:
    def __init__(self,datas):
        self.set_values(datas)

    def set_values(self,datas):
        """Set the values of all the fields

        At first defaulta value are created and they ar replaced
        by new values if found."""

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

    
    
