def solve():
    A,B,C = map(int,input().split())
    print(A+B+C+max(A,B,C)*9)

if __name__ == '__main__':
    solve()