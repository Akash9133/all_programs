class Address:
    __address:str=""
    def _init_(self):
        pass

    def setAddress(self,address: str):
        self.address = address

    def getAddress(self) -> str:
        return self.address

address = Address()
address.setAddress("3-100/23/1,NIZAMBAD")
print(address.getAddress())

class Employee(Address):
    __fName:str = ""
    __lName:str = ""
    __address:str = ""
    def __init__(self,fName,lName):
        super()._init_()
        self.__fName = fName
        self.__lName = lName

    def getFullName(self) -> str:
      return f'Full Name: {self.__fName} {self.__lName}'

    def salCal(self) -> float:
        pass
class PerminentEmp(Employee):
    __sal:float = 12000
    def __init__(self,fName,lName):
        super().__init__(fName,lName)
        pass

    def salCal(self) -> float:
        return self.__sal * 12

class ContractEmp(Employee):
    __sal: float = 1000
    def __init__(self,fName,lName):
        super().__init__(fName,lName)
        pass

    def salCal(self, hrs: int) -> float:
        return self.__sal*hrs

emp = PerminentEmp("Star","Akash")
name = emp.getFullName()
print(name)
emp.setAddress("NIZAMBAD")
address = emp.getAddress()
print(address)
print(emp.salCal())

emp = ContractEmp("naveen","alisheety")
name = emp.getFullName()
print(name)
emp.setAddress("nizambad")
address = emp.getAddress()
print(address)
print(emp.salCal(10))
