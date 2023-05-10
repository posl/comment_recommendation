def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j <= N:
                if (i*j)**0.5 == int((i*j)**0.5):
                    ans += 1
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()