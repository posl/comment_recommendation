def solve():
  n,a,b = map(int,input().split())
  for i in range(n):
    for j in range(a):
      for k in range(n):
        for l in range(b):
          if i%2 == 0:
            if k%2 == 0:
              print(".",end="")
            else:
              print("#",end="")
          else:
            if k%2 == 0:
              print("#",end="")
            else:
              print(".",end="")
        print("")
solve()
