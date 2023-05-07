def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    
    ans = X
    for i in range(101):
        if (X - i) not in p:
            ans = X - i
            break
        elif (X + i) not in p:
            ans = X + i
            break
    
    print(ans)
