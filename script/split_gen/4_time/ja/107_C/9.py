def solve(n,k,x):
  ans = 10**9
  for i in range(n-k+1):
    l = x[i]
    r = x[i+k-1]
    if l*r >= 0:
      ans = min(ans,max(abs(l),abs(r)))
    else:
      ans = min(ans,abs(l)+r+min(abs(l),abs(r)))
  return ans
n,k = map(int,input().split())
x = list(map(int,input().split()))
print(solve(n,k,x))
