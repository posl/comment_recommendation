def main():
    X,Y,Z,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    ans = []
    for a in A:
        for b in B:
            for c in C:
                ans.append(a+b+c)
    ans.sort(reverse=True)
    for i in range(K):
        print(ans[i])

if __name__ == '__main__':
    main()