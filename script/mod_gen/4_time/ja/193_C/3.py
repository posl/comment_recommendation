def main():
    N = int(input())
    ans = N
    for i in range(2, int(N**0.5)+1):
        for j in range(2, int(N**0.5)+1):
            if i**j <= N:
                ans -= 1
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()