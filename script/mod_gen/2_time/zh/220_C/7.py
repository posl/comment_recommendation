def solve():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A*100
    s = 0
    for i in range(1, 10**5+1):
        s += B[i-1]
        if s > X:
            print(i)
            break

if __name__ == '__main__':
    solve()