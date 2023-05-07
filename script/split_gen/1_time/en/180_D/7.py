def main():
    X,Y,A,B = map(int,input().split())
    ans = 0
    while A*X < X+B and A*X < Y:
        X *= A
        ans += 1
    ans += (Y-1-X)//B
    print(ans)
