def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = [a % 200 for a in A]
    D = {}
    for i in range(N):
        if A[i] in D:
            print('Yes')
            print(1,i+1)
            print(len(D[A[i]]),*D[A[i]])
            return
        else:
            D[A[i]] = [i+1]
    print('No')
    return

if __name__ == '__main__':
    main()