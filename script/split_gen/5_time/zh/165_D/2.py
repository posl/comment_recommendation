def solution():
    A,B,N = map(int, input().split())
    ans = 0
    x = min(B-1,N)
    ans = (A*x)//B - A*(x//B)
    return ans
