def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A = [a % 200 for a in A]
    D = {}
    for i in range(N):
        if A[i] in D:
            D[A[i]].append(i)
        else:
            D[A[i]] = [i]
    for a in D:
        if len(D[a]) >= 2:
            print("Yes")
            print(1, D[a][0]+1)
            print(1, D[a][1]+1)
            return
    for a in D:
        for b in D:
            if a == b: continue
            if (a+b) % 200 == 0:
                print("Yes")
                print(2, D[a][0]+1, D[b][0]+1)
                return
    print("No")

if __name__ == '__main__':
    main()