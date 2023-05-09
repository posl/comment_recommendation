def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        S,T = input().split()
        s.append(S)
        t.append(T)
    for i in range(N):
        for j in range(N):
            if i != j and s[i] == t[j]:
                print("No")
                exit()
    print("Yes")
