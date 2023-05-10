def main():
    S = input()
    Q = int(input())
    lst = []
    for i in range(Q):
        t, k = map(int, input().split())
        lst.append((t, k))
    #print(lst)
    for i in range(Q):
        t, k = lst[i]
        t = t % 3
        #print(t, k)
        if t == 0:
            print(S[k-1])
        elif t == 1:
            if k <= len(S):
                print(S[k-1])
            else:
                print(S[k-1 - len(S)])
        else:
            if k <= len(S):
                print(S[k-1])
            else:
                print(S[k-1 - len(S) * 2])

if __name__ == '__main__':
    main()