def main():
    N = input()
    N = list(N)
    N.sort()
    if N[0] == '0':
        for i in range(len(N)):
            if N[i] != '0':
                N[0], N[i] = N[i], N[0]
                break
    if N[0] == '0':
        print(-1)
    else:
        N = list(map(int, N))
        if sum(N) % 3 == 0:
            print(0)
        else:
            for i in range(len(N)):
                if N[i] % 3 == sum(N) % 3:
                    print(1)
                    break
            else:
                for i in range(len(N)):
                    for j in range(i+1, len(N)):
                        if (N[i] + N[j]) % 3 == sum(N) % 3:
                            print(2)
                            break
                    else:
                        continue
                    break
                else:
                    print(-1)

if __name__ == '__main__':
    main()