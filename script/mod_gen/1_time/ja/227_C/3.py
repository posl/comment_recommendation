def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**(1/3))+1):
        for j in range(i, int(N**(1/3))+1):
            for k in range(j, int(N**(1/3))+1):
                if i*j*k <= N:
                    ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()