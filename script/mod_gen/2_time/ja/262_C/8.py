def main():
  N = int(input())
  A = list(map(int, input().split()))
  #print(N, A)
  count = 0
  for i in range(1, N+1):
    if A[i-1] >= i:
      count += 1
  print(count)

if __name__ == '__main__':
    main()