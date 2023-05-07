def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    #print(A)
    #print(A[X])
    #print(A[A[X]])
    #print(A[A[A[X]]])
    ans = 0
    ans_list = []
    ans_list.append(X)
    ans_list.append(A[X])
    ans_list.append(A[A[X]])
    ans_list.append(A[A[A[X]]])
    #print(ans_list)
    for i in range(4, N+1):
        if A[ans_list[i-1]] in ans_list:
            ans = i
            break
        else:
            ans_list.append(A[ans_list[i-1]])
            #print(ans_list)
    print(ans)
