class employee():
    workplacename="Pickle Juice Factory"
    def __init__(self,eage,enumber,epassword,ename):
        self.epassword= epassword
        self.ename = ename
        self.eage =eage
        self.enumber=enumber

    def showdetails(self):
        print("name:"+self.ename)
        print("age:"+str(self.eage))
        print("number:{}".format(self.enumber))

    def login(self,p):
        if p == self.epassword:
            print("Login Succesful")
        else:
            print("Incorrect password")


E1=employee(35,97,"hello","spooder")
print(E1.ename)
print(E1.eage)
print(E1.enumber)
print(E1.workplacename)
E1.showdetails()
b=input("What is the password?")
E1.login(b)

