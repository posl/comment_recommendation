def main():
  n = int(input())
  a = list(map(int, input().split()))
  ans = 0
  for i in range(n):
    if a[i] == i + 1:
      continue
    if a[a[i] - 1] == i + 1:
      ans += 1
  print(ans)

if __name__ == '__main__':
    main()