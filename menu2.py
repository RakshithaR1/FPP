class menu:
  def __init__(self):
    self.item = {}
    
  def show(self):
    print(self.item)
    
m = menu()
m + ("idly",10) + ("vada",20)
m.show()