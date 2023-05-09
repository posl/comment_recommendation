def main():
    # Take input Here and Call solution function
    N = int(input())
    S = []
    for _ in range(N):
        S.append(tuple(map(int,input().split())))
    T = []
    for _ in range(N):
        T.append(tuple(map(int,input().split())))
    print(solution(N,S,T))
