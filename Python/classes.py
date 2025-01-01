class login():
    def __init__(self):
        self.username = "admin"
        self.password = "admin"

    def __debconnectivity(self, username,password):
        if username == self.username and password == self.password:
            print("Database connected Succesfully")
            print("Login Succesful")

        else:
            print("Login And DB Connectivity Failed")
    
    def updatePassword(self,newPassword):
        self.password = newPassword
        print("Password Updated")



    def logingIn(self, username,password):
        self.__debconnectivity(username,password)


user = login()
user.logingIn("admin","admin")

class addition:
    
    def add(self,x:int , y:int) -> int:
        pass

    def add(self,x:float , y:int) -> float:
        pass

    def add(self, x:str , y:str) -> str:
        pass


    def adder(self,x,y):
        if isinstance(x,int) and isinstance(y,int):
            return x + y
        
        if isinstance(x,float) and isinstance(y,int):
            return x + y
        
        if isinstance(x,str) and isinstance(y,str):
            return x + y
        
trio = addition()
print(trio.adder(10,2))
print(trio.adder("hello","world"))
print(trio.adder(10.4,2))
