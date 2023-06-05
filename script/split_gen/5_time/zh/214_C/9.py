def main():
    N = int(input())
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))
    for i in range(N):
        T[i] = [T[i],i]
    T.sort()
    for i in range(N):
        T[i] = T[i][1]
    for i in range(N):
        if i == 0:
            time = 0
        else:
            time = max(time,S[T[i-1]])
        print(time)
