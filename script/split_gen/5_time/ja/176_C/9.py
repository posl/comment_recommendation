def main():
  N = int(input())
  A = list(map(int, input().split()))
  ans = 0
  for i in range(N-1, -1, -1):
    if A[i] <= ans:
      ans = A[i]
    else:
      ans = A[i] - 1
  print(ans)
