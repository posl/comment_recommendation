def main():
  n = int(input())
  a = list(map(int, input().split()))
  q = int(input())
  for _ in range(q):
    l, r, x = map(int, input().split())
    print(sum(1 for i in range(l-1, r) if a[i] == x))
main()
