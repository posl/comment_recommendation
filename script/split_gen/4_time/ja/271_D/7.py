def main():
  N, S = map(int, input().split())
  cards = [list(map(int, input().split())) for _ in range(N)]
  for i in range(2 ** N):
    count = 0
    sum = 0
    ans = ""
    for j in range(N):
      if ((i >> j) & 1):
        count += 1
        sum += cards[j][0]
        ans += "H"
      else:
        sum += cards[j][1]
        ans += "T"
    if count == N and sum == S:
      print("Yes")
      print(ans)
      return
  print("No")
  return
