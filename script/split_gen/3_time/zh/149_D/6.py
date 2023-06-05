def cal(N,K,R,S,P,T):
    sum = 0
    for i in range(N):
        if T[i] == 'r':
            if i >= K and T[i-K] == 'r':
                T[i] = 'p'
            else:
                sum += P
        elif T[i] == 's':
            if i >= K and T[i-K] == 's':
                T[i] = 'r'
            else:
                sum += R
        else:
            if i >= K and T[i-K] == 'p':
                T[i] = 's'
            else:
                sum += S
    return sum
N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())
print(cal(N,K,R,S,P,T))
