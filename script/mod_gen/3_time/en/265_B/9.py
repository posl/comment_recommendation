def main():
  N, M, T = map(int, input().split())
  A = list(map(int, input().split()))
  B = [0] * (N-1)
  for i in range(N-1):
    B[i] = T - A[i]
  for i in range(M):
    X, Y = map(int, input().split())
    B[X-1] += Y
  for i in range(N-1):
    if B[i] <= 0:
      print("No")
      return
  print("Yes")
  return

if __name__ == '__main__':
    main()