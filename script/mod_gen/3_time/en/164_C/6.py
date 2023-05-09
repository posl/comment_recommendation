def main():
    N = int(input())
    S = [input() for i in range(N)]
    S = set(S)
    print(len(S))

if __name__ == '__main__':
    main()