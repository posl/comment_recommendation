def main():
  n = int(input())
  ans = 0
  for a in range(1, int(n ** 0.5) + 1):
    for b in range(a, int(n ** (1/3)) + 1):
      for c in range(b, int(n ** 0.25) + 1):
        if a * b * c <= n:
          ans += 1
        else:
          break
  print(ans)

if __name__ == '__main__':
    main()