def solve():
    #K = int(input())
    #A, B = map(int, input().split())
    K = 7
    A = 500
    B = 600
    if K % A == 0 or K % B == 0:
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    solve()