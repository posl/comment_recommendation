def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(max(S, key=S.count))

if __name__ == '__main__':
    main()