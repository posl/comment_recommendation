def solve():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    #累積和
    s = [0]*(N+1)
    for i in range(N):
        s[i+1] = s[i] + A[i]
    #Qを固定して考える
    #Qより前にPより大きい値があると条件を満たす組が存在する
    #Qより後にRより大きい値があると条件を満たす組が存在する
    #Qより後にPより小さい値があると条件を満たす組が存在する
    #Qより前にRより小さい値があると条件を満たす組が存在する
    #Qより前にPより大きくRより大きい値があると条件を満たす組が存在する
    #Qより後にPより小さくRより小さい値があると条件を満たす組が存在する
    #Qより前にPより大きくRより小さい値があると条件を満たす組が存在する
    #Qより後にPより小さくRより大きい値があると条件を満たす組が存在する
    #Qより前にPより大きい値があると条件を満たす組が存在する
    for i in range(N):
        if s[i] > P:
            break
        if s[i] < P:
            continue
        for j in range(i+1,N):
            if s[j] > P:
                break
            if s[j] < P:
                continue
            if s[j] - s[i] == P:
                for k in range(j+1,N):
                    if s[k] > Q:
                        break
                    if s[k] < Q:
                        continue
                    if s[k] - s[j] == Q:
                        for l in range(k+1,N
