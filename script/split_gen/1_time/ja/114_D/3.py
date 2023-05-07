def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if (N//i)%2 == 1 and (N//i)%3 == 1 and (N//i)%5 == 1:
            ans += 1
    print(ans)
