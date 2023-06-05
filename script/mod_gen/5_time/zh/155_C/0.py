def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = list(set(S))
    S.sort()
    for i in range(len(S)):
        print(S[i])

if __name__ == '__main__':
    main()