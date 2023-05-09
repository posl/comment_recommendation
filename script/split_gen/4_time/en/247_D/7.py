def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(input().split())
    q = q[::-1]
    ans = []
    s = 0
    for i in range(n):
        if q[i][0] == "2":
            s += int(q[i][1])
            ans.append(s)
        else:
            s = 0
    ans = ans[::-1]
    for i in ans:
        print(i)
