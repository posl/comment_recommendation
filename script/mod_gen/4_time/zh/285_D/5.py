def solve():
    N = int(input())
    s = [0]*N
    t = [0]*N
    for i in range(N):
        s[i],t[i] = input().split()
    for i in range(N):
        for j in range(N):
            if i != j and s[i] == t[j]:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    solve()