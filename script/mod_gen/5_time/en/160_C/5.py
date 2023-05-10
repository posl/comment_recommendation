def main():
  K, N = map(int, input().split())
  A = list(map(int, input().split()))
  max_dist = 0
  for i in range(N):
    if i == 0:
      max_dist = max(max_dist, K - A[i] + A[i+1])
    elif i == N - 1:
      max_dist = max(max_dist, A[i] - A[i-1] + K - A[i])
    else:
      max_dist = max(max_dist, A[i] - A[i-1], K - A[i] + A[i+1])
  print(K - max_dist)

if __name__ == '__main__':
    main()