class Person:
    def __init__(self,datas):
        self.name = datas['fn']
        self.address = datas['adr']
        self.phone = datas['tel']
        self.email = datas['email']
        self.photo = datas['photo']
        self.org = datas['org']

        #For easy setting and getting value
        self.mapping = {'name':self.name,
                   'phone':self.phone,
                   'email':self.email,
                   'address':self.address,
                   'org':self.org}
        
    def getValue(self,fieldname):
        '''Returns the value of specific attributes of the
        contact object'''
        return self.mapping[fieldname]
        

    def setValue(self,fieldname,value):
        '''Set the value of an object attributes as provided
        in the parameter'''
        #Not Done

    
