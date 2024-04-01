import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
op = input("Enter the operation to be performed (+,-,*,/,//,** and sqrt for square root): ")
result=0
if(op == '+'):
  result = a+b
elif(op == '-'):
  result = a-b
elif(op == '*'):
  result = a*b
elif(op == '/'):
  result = a/b
elif(op == '%'):
  result = a%b
elif(op == 'sqrt'):
  result = []
  result.append(math.sqrt(a))
  result.append(math.sqrt(b))
elif(op == '//'):
  result = a//b
elif(op == '**'):
  result = a**b
else:
  print("Enter the right operator")
  exit()

print(f"The result of the operation performed on {a} and {b} is {result}")