def main():
  #N = int(input())
  #LR = [list(map(int, input().split())) for _ in range(N)]
  N = 3
  LR = [[10, 20], [20, 30], [40, 50]]
  #N = 3
  #LR = [[10, 40], [30, 60], [20, 50]]
  LR.sort(key=lambda x: x[0])
  #print(LR)
  ans = []
  ans.append(LR[0])
  for l, r in LR[1:]:
    if l <= ans[-1][1]:
      ans[-1][1] = max(ans[-1][1], r)
    else:
      ans.append([l, r])
  for l, r in ans:
    print(l, r)
  return
