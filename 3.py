def input_n():
  n = int(input("Enter the value of n: "))
  return n
def input_num(n,a):
  for i in range(n):
    a.append(int(input("Enter the numbers: ")))

def sum_n_num(a):
  return sum(a)
def output(sum):
  print(f"The sum of the given numbers are: {sum} " )


a = []
n = input_n()
input_num(n,a)
result = sum_n_num(a)
output(result)



