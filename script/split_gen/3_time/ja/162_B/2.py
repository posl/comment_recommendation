def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if i%3 == 0 and i%5 == 0:
            ans += 0
        elif i%3 == 0:
            ans += 0
        elif i%5 == 0:
            ans += 0
        else:
            ans += i
    print(ans)
