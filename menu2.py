class menu:
    def __init__(self,items,price):
        self.items=items
        self.price=price
    def show (self):
        print(self.items,self.price)
menu1=menu("dosa",50)
menu2=menu("idli",40)
menu1.show()
menu2.show()
