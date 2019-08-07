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
        return self.mapping[fieldname]
        

    def setValue(self,fieldname,value):
        self.mapping[fieldname] = value
        #Its wrong
    
