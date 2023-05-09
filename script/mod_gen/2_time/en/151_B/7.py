def main():
  n, k, m = map(int, input().split())
  a = list(map(int, input().split()))
  avg = m*n - sum(a)
  if avg <= 0:
    print(0)
  elif avg > k:
    print(-1)
  else:
    print(avg)

if __name__ == '__main__':
    main()