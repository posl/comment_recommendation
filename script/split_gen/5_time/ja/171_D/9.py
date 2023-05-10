def main():
  n = int(input())
  a = list(map(int, input().split()))
  q = int(input())
  b = []
  c = []
  for i in range(q):
    b_c = list(map(int, input().split()))
    b.append(b_c[0])
    c.append(b_c[1])
  for i in range(q):
    for j in range(n):
      if a[j] == b[i]:
        a[j] = c[i]
    print(sum(a))
