def main():
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  a.sort(reverse=True)
  total = sum(a)
  if a[m-1] >= total / (4 * m):
    print("Yes")
  else:
    print("No")
main()

if __name__ == '__main__':
    main()