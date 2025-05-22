class Bank:
    bank_name = "State Bank"

    @classmethod
    def chnge_bank_name(cls, name):
        cls.bank_name = name


b1 = Bank()
print(b1.bank_name)  
b1.chnge_bank_name("National Bank")
print(b1.bank_name) 
