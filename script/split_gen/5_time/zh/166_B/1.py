def main():
    N,K = map(int,input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int,input().split())))
    #print(N,K,d,A)
    count = 0
    for i in range(N):
        flag = 0
        for j in range(K):
            if i+1 in A[j]:
                flag = 1
                break
        if flag == 0:
            count += 1
    print(count)
