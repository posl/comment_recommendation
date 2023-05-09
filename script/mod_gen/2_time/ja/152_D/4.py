def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i%10 == j//10**int(len(str(j)))-1:
                ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()