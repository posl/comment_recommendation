def main():
  N = int(input())
  S = list(map(int, input().split()))
  A = [0] * N
  for i in range(N):
    if i % 2 == 0:
      A[0] += S[i]
    else:
      A[0] -= S[i]
  for i in range(N - 1):
    A[i + 1] = 2 * S[i] - A[i]
  print(*A)
