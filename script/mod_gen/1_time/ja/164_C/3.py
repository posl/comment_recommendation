def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(len(set(S)))

if __name__ == '__main__':
    main()