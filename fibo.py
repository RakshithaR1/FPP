a,b=0,1
n=int(input("Enter the fibonacci value to be found: "))
series = [0]
for i in range(n):
  
 a,b=b,a+b
 series.append(a)

print(series)


