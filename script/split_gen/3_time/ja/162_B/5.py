def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if i%15==0:
            ans += i
        elif i%3==0:
            ans += i
        elif i%5==0:
            ans += i
    print(ans)
