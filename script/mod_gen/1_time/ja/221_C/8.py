def main():
    N = input()
    N = list(map(int, N))
    N.sort(reverse = True)
    N = list(map(str, N))
    N = ''.join(N)
    N = int(N)
    N = str(N)
    N = list(N)
    N = list(map(int, N))
    print(N[0] * N[1])

if __name__ == '__main__':
    main()