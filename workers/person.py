import re
class Person:
    phones=[]
    firstName=""
    lastName=""
    ID=0

    @staticmethod
    def emailCheck(email):  # func to check the email
        return re.match("^[a-zA-Z]*@([a-zA-Z]*.)+hwltd.com$", email)
    @classmethod
    def IDNum(cls):  # func for running number
        cls.ID = cls.ID + 1
        return cls.ID
    def __init__(self, firstName, lastName, yearOfBirth, email, phones, addr): #person constructor
        if (firstName == "" or lastName == ""): #first and last name must not be empty
            raise ("missing first or last name")
        else:
            self.firstName= (firstName)
            self.lastName = (lastName)
        if (self.emailCheck(email)): #check the email
            self.email = (email)
        else:
            raise("incorrect email")
        self.yearOfBirth=yearOfBirth
        self.phones=phones
        self.addr=addr
        self.ID=self.IDNum()

    def phoneRemove(self,phone): #remove a phone from the phones list
        self.phones.remove(phone)
    def phoneAdd(self,phone): #add a phone to the phones list
        self.phones.append(phone)


class Phone:
    def __init__(self, number): #phone constructor
        num=number
        if (re.match("^[+]?([0-9]|[-])*$", str(num))):
            self.number= number
class Address:
    def __init__(self, country, city): #address constructor
        if(country!="" and city!=""):
            self.country = country
            self.city = city
        else:
            raise("missing country or city")
    def _otherDetails(self): #abstruct method for more details
        raise NotImplementedError("Please Implement this method")
    def addressDetails(self): #print the address details
        print("address details:/n"+self.country+"/n"+self.city+"/n"+self.otherDetails())


class StreetAddress(Address): #inherrits address
   def  __init__(self, streetName, houseNumber, country, city): # StreetAddress constructor
       self.streetName=streetName
       self.houseNumber=houseNumber
       super(StreetAddress, self).__init__(country, city) #base constructor
   def _otherDetails(self): #implement the abstruct method
       return self.streetName+" "+self.houseNumber

class PobAddress(Address): #inherrits address
    def __init__(self, pobNumber,country,city): #PobAddress constructor
        self.pobNumber=pobNumber
        super(PobAddress, self).__init__(country, city) #base constructor
    def _otherDetails(self): #implement the abstruct method
        return self.pobNumber

def main():
    print("Hello World!")
    p1 = Person("aaa","ccc",1998,"ura@mng.hwltd.com", [123], "r ")
    p2 = Person("qwe", "zzz", 2020, "lauljkhghra@mng.hwltd.com", [147852-69],"sa")
    ph1 = Phone(123456)
    ph2 = Phone(34667)
    ph3 = Phone(987654)
    p1.phones.append(ph1)
    p1.phones.append(ph2)
    p1.phones.append(ph3)
    p1.phoneAdd(987)
    for n in p1.phones:
        print(n)
    print(p1.email)
    print(p1.addr)
    ph = Phone("+64-7617201")
    print(ph.number)
    print(p1.ID)
    print(p2.ID)
    a = Address("israel", "betar")
    print(a.addressDetails())
    s = StreetAddress(104, "kdushat", "israel", "betar")
    if __name__ == '__main__':
        main()