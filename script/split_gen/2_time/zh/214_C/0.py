def main():
    N = int(input())
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))
    S.insert(0,0)
    T.insert(0,0)
    for i in range(1,N+1):
        if i == 1:
            print(T[i])
        elif i == N:
            if T[i-1] + S[i-1] > T[i]:
                print(T[i])
            else:
                print(T[i-1] + S[i-1])
        else:
            if T[i-1] + S[i-1] > T[i]:
                print(T[i])
            else:
                print(T[i-1] + S[i-1])
