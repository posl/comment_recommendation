def main():
    N = int(input())
    ans = 0
    for i in range(N):
        if '7' not in str(i+1) and '7' not in oct(i+1):
            ans += 1
    print(ans)
main()
