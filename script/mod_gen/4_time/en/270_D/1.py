def main():
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  stones = [0] * (N + 1)
  for i in range(1, N + 1):
    for a in A:
      if i >= a:
        stones[i] = (stones[i] + stones[i - a]) % 1000000007
      elif a > i:
        break
    if i in A:
      stones[i] = (stones[i] + 1) % 1000000007
  print(stones[N])

if __name__ == '__main__':
    main()