class Demo:

    def __init__(self):
        print("This is my first class tutorial")

    def add_num(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1+self.num2

demo = Demo()   
print(demo.add_num(5,6))