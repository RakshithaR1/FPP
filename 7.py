dict = {'a':'b','c':'d','e':'f','g':'h'}
cs=()
arr=[]
for key,value in dict.items():
  cs=(key,value)
  arr.append(cs)
print(arr)
result = ";".join(["=".join(ele) for ele in arr])
print(result)
                  
