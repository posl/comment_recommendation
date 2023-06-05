def main():
    # read input
    A, B, N = map(int, input().split())
    #print(A, B, N)
    # solve the problem
    ans = 0
    x = min(B-1, N)
    ans = (A*x)//B - A*(x//B)
    # output
    print(ans)
