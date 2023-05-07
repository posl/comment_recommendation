def main():
    a,b = map(int,input().split())
    ans = 1
    for i in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            ans += 1
    print(ans)
