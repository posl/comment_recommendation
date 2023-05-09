def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N**0.5)+1):
        for j in range(2, int(N**0.5)+1):
            if i**j <= N:
                ans += 1
            else:
                break
    print(N-ans)

if __name__ == '__main__':
    main()