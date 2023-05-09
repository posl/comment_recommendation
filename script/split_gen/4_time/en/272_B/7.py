def main():
    N,M = map(int,input().split())
    A = []
    for _ in range(M):
        A.append(list(map(int,input().split()))[1:])
    flag = True
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                tmp = False
                for k in range(M):
                    if i+1 in A[k] and j+1 in A[k]:
                        tmp = True
                        break
                if not tmp:
                    flag = False
                    break
    if flag:
        print("Yes")
    else:
        print("No")
