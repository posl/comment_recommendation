def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort(key=lambda s: [X.find(c) for c in s])
    print('\n'.join(S))

if __name__ == '__main__':
    main()