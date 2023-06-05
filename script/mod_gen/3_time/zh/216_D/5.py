def main():
    N,M = map(int,input().split())
    A = []
    for i in range(M):
        k = int(input())
        a = list(map(int,input().split()))
        A.append(a)
    A.sort(key = lambda x:x[0])
    #print(A)
    flag = True
    for i in range(M-1):
        if A[i][0] == A[i+1][0]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()