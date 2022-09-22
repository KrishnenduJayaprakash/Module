class employee:
    eid=0
    ename=""
    dept=""
    basic=""
    nol=0
    
    def __init__(self):
    #def input(self):
        self.eid=int(input("Enter the id: "))
        self.ename=input("Enter the name: ")
        self.dept=input("Enter the department: ")
        self.basic=int(input("Enter the basic salary: "))
        self.nol=int(input("Enter the no of leaves: "))
        
        
    def showemp(self):
         print("EID: ",self.eid)
         print("Ename: ",self.ename)
         print("Department: ",self.dept)
         print("Basic salary: ",self.basic)
         print("No of leaves taken: ",self.nol)
        
    def calc(self):
        hra=self.basic*10/100
        cca=self.basic*12/100
        pf=self.basic*5/100
        lamt=(self.basic/30)*self.nol
        gsal=hra+cca+self.basic
        netsal=gsal-pf-lamt
        print("Net salary: ",netsal)
        
    
ob=employee()
#ob.input()
ob.showemp()
ob.calc()


#OUTPUT:
Enter the id: 1001
Enter the name: Ravi
Enter the department: CSE
Enter the basic salary: 30000
Enter the no of leaves: 2
EID:  1001
Ename:  Ravi
Department:  CSE
Basic salary:  30000
No of leaves taken:  2
Net salary:  33100.0
