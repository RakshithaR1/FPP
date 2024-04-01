list = [('a','b'),('c','d'),('e','f'),('g','h')]
def listtocs(list):
  res = ';'.join(['='.join(ele) for ele in list])
  print(res)
listtocs(list)