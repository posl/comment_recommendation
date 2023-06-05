Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        x,y = map(int,input().split())
        l.append(x)
        r.append(y)
    l.sort()
    r.sort()
    print(l[0],r[-1])

=======
Suggestion 2

def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)

    l.sort()
    r.sort()

    print(l[0], r[-1])

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        l, r = map(int, input().split())
        s.append([l, r])
    s.sort()
    ans = []
    left = s[0][0]
    right = s[0][1]
    for i in range(1, n):
        if right < s[i][0]:
            ans.append([left, right])
            left = s[i][0]
            right = s[i][1]
        else:
            right = max(right, s[i][1])
    ans.append([left, right])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 4

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

=======
Suggestion 5

def main():
    n = int(input())

    # 读取输入
    l = []
    r = []
    for i in range(n):
        line = input()
        l.append(int(line.split()[0]))
        r.append(int(line.split()[1]))

    # 按照左端点排序
    l.sort()
    r.sort()

    # 合并区间
    ans = []
    begin = l[0]
    end = r[0]
    for i in range(1, n):
        if l[i] <= end:
            end = r[i]
        else:
            ans.append([begin, end])
            begin = l[i]
            end = r[i]
    ans.append([begin, end])

    # 打印
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 6

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    left = l[0][0]
    right = l[0][1]
    for i in range(1, n):
        if l[i][0] <= right:
            right = max(right, l[i][1])
        else:
            print(left, right)
            left = l[i][0]
            right = l[i][1]
    print(left, right)

=======
Suggestion 7

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    x = l[0][0]
    y = l[0][1]
    for i in range(1, n):
        if y < l[i][0]:
            print(x, y)
            x = l[i][0]
            y = l[i][1]
        elif y < l[i][1]:
            y = l[i][1]
    print(x, y)

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    n = int(input())
    lr_list = []
    for _ in range(n):
        l, r = map(int, input().split())
        lr_list.append((l, r))
    lr_list.sort()
    ans = []
    l, r = lr_list[0][0], lr_list[0][1]
    for i in range(1, n):
        if lr_list[i][0] <= r:
            r = max(r, lr_list[i][1])
        else:
            ans.append((l, r))
            l, r = lr_list[i][0], lr_list[i][1]
    ans.append((l, r))
    print(*ans, sep='\n')
