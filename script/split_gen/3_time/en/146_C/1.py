def main():
    #input
    A, B, X = map(int, input().split())
    #compute
    if A * 10**9 + B * 10 <= X:
        ans = 10**9
    else:
        ans = 0
        for i in range(1, 10):
            if A * 10**(i-1) + B * i <= X:
                ans = max(ans, 10**(i-1) + (X - A * 10**(i-1) - B * i) // (A * 10**(i-1) + B * i))
    #output
    print(ans)
