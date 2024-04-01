def input_low():
  low = int(input("Enter the lower limit: "))
  return low
def input_up():

    up = int(input("Enter the upper limit: "))
    return up
def sum_num(low,up):

  sum=0
  for i in range(low,up):
    sum += i
  return sum

def output(low,up,sum):
 print(f"The sum of numbers between {low} and {up} is {sum}")

low=input_low()
up=input_up()

result = sum_num(low,up)
output(low,up,result)
