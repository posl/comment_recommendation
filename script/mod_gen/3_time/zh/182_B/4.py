def gcd(a,b):
  if b == 0: return a
  return gcd(b,a%b)
n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(2,1001):
  tmp = 0
  for j in range(n):
    if a[j]%i == 0: tmp += 1
  if tmp >= ans:
    ans = tmp
    ans_num = i
print(ans_num)

if __name__ == '__main__':
    gcd()