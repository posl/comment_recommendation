def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    ans = 0
    #Aの最大値がX回未満であれば、AのみのゲームをX回行う
    if X <= N:
        ans = sum(A[0:X])
    else:
        ans = sum(A)
        X -= N
        #Bの最大値がX回未満であれば、BのみのゲームをX回行う
        if X <= N:
            ans += sum(B[0:X])
        else:
            ans += sum(B)
            X -= N
            #Aの最大値とBの最大値の和がX回未満であれば、AとBのゲームをX回行う
            if X <= N:
                ans += (A[-1] + B[-1]) * X
            else:
                ans += (A[-1] + B[-1]) * N
    print(ans)

if __name__ == '__main__':
    main()