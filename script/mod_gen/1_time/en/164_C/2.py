def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    print(len(S))

if __name__ == '__main__':
    main()