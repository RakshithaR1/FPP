dict = {'a':'b','c':'d','e':'f','g':'h'}

arr=[]
for key,value in dict.items():
  arr.append(key+"="+value)
print(arr)
result = ";".join(arr)
print(result)
                  
