def main():
    N,Q = [int(i) for i in input().split()]
    S = input()
    S = list(S)
    S.reverse()
    for i in range(Q):
        t,x = [int(i) for i in input().split()]
        if t == 1:
            for j in range(x):
                S.append(S.pop())
        else:
            print(S[x-1])

if __name__ == '__main__':
    main()