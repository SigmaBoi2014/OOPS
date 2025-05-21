class student():
    schoolname="David Lloyd George"
    def __init__(self,sname,sage,snumber):
        self.sname = sname
        self.sage =sage
        self.snumber=snumber
s1=student("axl",11,67)
print(s1.sname)
print(s1.sage)
print(s1.snumber)
print(s1.schoolname)