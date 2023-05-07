def main():
    A,B = map(int,input().split())
    ans = 0
    ans = A/(2**0.5)
    for i in range(1,B+1):
        ans = min(ans,i + A/((2**i)**0.5))
    print(ans)
