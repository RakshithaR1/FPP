arr = "a=b;c=d;e=f;g=h"
dict = {}
def cstodict(arr):
  for i in arr.split(";"):
     x=i.split("=")
     dict.update({x[0]:x[1]})
     
  print(dict)
cstodict(arr)

print({j[0]:j[1] for j in [i.split("=") for i in arr.split(";")]})

  
  