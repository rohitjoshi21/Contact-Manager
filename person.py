class Person:
    def __init__(self,datas):
        self.name = datas['fn']
        self.address = datas['adr'] if 'adr' in datas else None
        self.phone = datas['tel'] if 'tel' in datas else None
        self.email = datas['email'] if 'email' in datas else None
        self.photo = datas['photo'] if 'photo' in datas else None
        self.org = datas['org'] if 'org' in datas else None
    
    def getValue(self,fieldname):
        '''Returns the value of specific attributes of the
        contact object'''
        return getattr(self,fieldname)
        

    def setValue(self,fieldname,value):
        '''Set the value of an object attributes as provided
        in the parameter'''
        setattr(self,fieldname,value)

    
        
