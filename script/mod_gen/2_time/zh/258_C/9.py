def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            S = S[-1] + S[:-1]
        else:
            print(S[int(query[1])-1])

if __name__ == '__main__':
    main()