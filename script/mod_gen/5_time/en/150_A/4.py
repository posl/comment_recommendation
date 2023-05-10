def solve():
    K,X = map(int,input().split())
    print("Yes" if X <= K*500 else "No")

if __name__ == '__main__':
    solve()