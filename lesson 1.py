class student():
    schoolname="David Lloyd George"
    def __init__(self,sname,sage,snumber,spassword):
        self.spassword= spassword
        self.sname = sname
        self.sage =sage
        self.snumber=snumber

    def showdetails(self):
        print("name:"+self.sname)
        print("age:"+str(self.sage))
        print("number:{}".format(self.snumber))
    
    def login(self,p):
        if p == self.spassword:
            print("Login Succesful")
        else:
            print("Incorrect password")




s1=student("axl",11,67,"hello")
print(s1.sname)
print(s1.sage)
print(s1.snumber)
print(s1.schoolname)
s1.showdetails()
s2=student("spoodey",12,30058895848,"hi")
s2.showdetails()
s1.login("hello")
s2.login("nhbhbhchndjcnecncjnj")
b=input("What is the password? ")
s2.login(b)