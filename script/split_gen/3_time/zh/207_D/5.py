def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(map(int,input().split())))
    for i in range(n):
        t.append(list(map(int,input().split())))
    s.sort(key=lambda x:x[0])
    t.sort(key=lambda x:x[0])
    for i in range(n):
        if s[i][0] != t[i][0] or s[i][1] != t[i][1]:
            print("No")
            return
    print("Yes")
