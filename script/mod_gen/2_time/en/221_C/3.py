def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N.sort(reverse=True)
    if N[0] == 1:
        print((N[0]+N[1]) * int("".join(map(str, N[2:]))))
    else:
        print(N[0] * int("".join(map(str, N[1:]))))

if __name__ == '__main__':
    main()