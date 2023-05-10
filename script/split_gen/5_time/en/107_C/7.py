def main():
  n,k = map(int,input().split())
  x = list(map(int,input().split()))
  ans = float('inf')
  for i in range(n-k+1):
    l = x[i]
    r = x[i+k-1]
    if l <= 0 and r <= 0:
      ans = min(ans,abs(l))
    elif l <= 0 and r >= 0:
      ans = min(ans,abs(l)*2+r,abs(r)*2+abs(l))
    else:
      ans = min(ans,abs(r))
  print(ans)
main()
