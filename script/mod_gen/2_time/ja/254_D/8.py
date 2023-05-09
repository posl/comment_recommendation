def main():
    N = int(input())
    #N = 254
    #N = 4
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i * j <= N:
                if int(i * j ** 0.5) == i * j ** 0.5:
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()