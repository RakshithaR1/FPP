class menu:
  def __init__(self):
    self.items = {}
    
  def add(self,item,price):
    self.items[item] = price
    
  def show(self):
    print(self.items)
  
m=menu()
m.add("idly",10)
m.add("vada",20)
m.show()


      