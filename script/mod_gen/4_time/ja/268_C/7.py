def main():
  N = int(input())
  P = list(map(int, input().split()))
  count = 0
  for i in range(N):
    if P[i] == i:
      count += 1
  if count == N:
    print(N)
  else:
    print(N-1)

if __name__ == '__main__':
    main()