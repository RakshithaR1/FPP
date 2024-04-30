class menu:
  def __init__(self):
    self.item = ()
    
  def show(self):
    menu_dict = {self.item[i] : self.item[i+1] for i in range(0,len(self.item),2)}
    print(menu_dict)
    
m = menu()
m + ("idly",10) + ("vada",20)
m.show()