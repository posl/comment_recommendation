def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(max(S, key=S.count))

if __name__ == '__main__':
    main()