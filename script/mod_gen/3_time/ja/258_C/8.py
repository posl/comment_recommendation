def main():
    N, Q = map(int, input().split())
    S = input()
    S = list(S)
    #print(S)
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S.insert(0, S.pop(x-1))
            #print(S)
        else:
            print(S[x-1])
            #print(S)

if __name__ == '__main__':
    main()