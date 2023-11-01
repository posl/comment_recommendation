def main():
    N = int(input())
    S = set()
    for i in range(N):
        S.add(input())
    print(len(S))

if __name__ == '__main__':
    main()