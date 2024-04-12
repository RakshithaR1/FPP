my_list = [1, 2, 3]

# Obtaining an iterator for my_list
iterator = iter(my_list)

# Looping over the iterator
while True:
    try:
        # Calling __next__() on the iterator
        item = iterator.__next__()
        print(item)  # Print the current item
    except StopIteration:
        break  # Exit the loop when StopIteration is raised
      
class MyIterator:
    a=10
    def __init__(self):
        self.current = 1
        
