def main():
    N,Q = map(int,input().split())
    S = input()
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            S = S[N-int(query[1]):N] + S[0:N-int(query[1])]
        else:
            print(S[int(query[1])-1])

if __name__ == '__main__':
    main()