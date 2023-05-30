def f(n):
  if n==0:
    return 0
  elif n<10:
    return n
  else:
    dig=len(str(n))
    return ((n-10**(dig-1)+1)*dig+f(10**(dig-1)-1))%998244353
n=int(input())
print((f(n))%998244353)
