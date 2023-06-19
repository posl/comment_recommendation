def main():
    N = input()
    k = len(N)
    if k == 1:
        if int(N) % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        for i in range(1, k):
            if int(N[i]) % 3 == 0:
                print(1)
                break
            else:
                if (int(N[i-1]) + int(N[i])) % 3 == 0:
                    print(2)
                    break
        else:
            print(-1)

if __name__ == '__main__':
    main()