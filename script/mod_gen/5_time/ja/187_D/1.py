def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    vote = []
    for i in range(n):
        vote.append(a[i]+b[i])
    #print(vote)
    vote.sort(reverse=True)
    #print(vote)
    aoki = 0
    takahashi = 0
    for i in range(n):
        if i%2 == 0:
            aoki += vote[i]
        else:
            takahashi += vote[i]
    #print(aoki)
    #print(takahashi)
    print(aoki - takahashi)

if __name__ == '__main__':
    main()