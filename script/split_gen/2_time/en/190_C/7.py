def get_input():
  n, m = map(int, input().split())
  ab = [list(map(int, input().split())) for _ in range(m)]
  k = int(input())
  cd = [list(map(int, input().split())) for _ in range(k)]
  return (n, m, ab, k, cd)
