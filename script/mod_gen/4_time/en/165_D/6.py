def solve(A, B, N):
  max = 0
  for i in range(N+1):
    tmp = A*i//B - A*(i//B)
    if tmp > max:
      max = tmp
  return max
A, B, N = map(int, input().split())
print(solve(A, B, N))

if __name__ == '__main__':
    solve()