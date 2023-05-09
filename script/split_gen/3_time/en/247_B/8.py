def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        st = input().split()
        s.append(st[0])
        t.append(st[1])
    if len(s) != len(set(s)) or len(t) != len(set(t)):
        print("No")
        return
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j] and t[i] == t[j]:
                print("No")
                return
    print("Yes")
