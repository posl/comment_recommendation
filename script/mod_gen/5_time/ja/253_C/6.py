def main():
  import sys
  def input(): return sys.stdin.readline().rstrip()
  from collections import defaultdict
  from heapq import heappush, heappop
  q = int(input())
  s = []
  d = defaultdict(int)
  for _ in range(q):
    query = input().split()
    if query[0] == '1':
      heappush(s, int(query[1]))
      d[int(query[1])] += 1
    elif query[0] == '2':
      while s and d[s[0]] == 0:
        heappop(s)
      if s:
        d[heappop(s)] -= 1
    else:
      while s and d[s[0]] == 0:
        heappop(s)
      print(s[-1] - s[0])
  return

if __name__ == '__main__':
    main()