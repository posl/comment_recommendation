def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #AとBが同じ値の場合は、その値でXを作れる
    for i in range(N):
        if A[i] == B[i]:
            continue
        #AとBの値が異なる場合、AとBの値の差がKを超える場合は、Xを作れない
        if abs(A[i] - B[i]) > K:
            print('No')
            return
    #AとBの値が異なる場合、AとBの値の差がKを超えない場合は、Xを作れる
    print('Yes')

if __name__ == '__main__':
    main()