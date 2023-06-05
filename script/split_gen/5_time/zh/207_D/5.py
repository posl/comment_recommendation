def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(map(int,input().split())))
    for i in range(n):
        t.append(list(map(int,input().split())))
    s.sort()
    t.sort()
    for i in range(n):
        for j in range(n):
            if s[j][0] == t[i][0] and s[j][1] == t[i][1]:
                break
            if j == n-1:
                print("No")
                exit()
    print("Yes")
