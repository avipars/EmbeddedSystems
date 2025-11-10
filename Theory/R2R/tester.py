def his(v1,v2,v3):
  return (2/253)*v1 + (1/506)*v2 + (1/1012) * v3

def mine(v1,v2,v3):
  return (16/2016) * (v1/2 + v2/4 + v3/8)


def chatgpt(v1,v2,v3):
  return (1/1008) * (4 * v1 + 2 * v2 + 1 * v3)


def runner(v1,v2,v3):
  print("V1 = ",v1)
  print("V2 = ",v2)
  print("V3 = ",v3)
  print("\n his")
  print(his(v1,v2,v3))
  print("\n mine")
  print(mine(v1,v2,v3))
  print("\n chatg")
  print(chatgpt(v1,v2,v3))


runner(552,25255,27)