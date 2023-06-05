def main():
  n, t = map(int, input().split())
  data = [[int(x) for x in input().split()] for _ in range(n)]
  data.sort(key=lambda x: x[1])
  ans = 1000
  for i in range(n):
    if data[i][1] <= t:
      ans = min(ans, data[i][0])
  if ans == 1000:
    print("TLE")
  else:
    print(ans)
main()
