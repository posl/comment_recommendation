def main():
    N = int(input())
    S = list(map(int,input().split()))
    A = []
    A.append(S[0])
    for i in range(1,N):
        A.append(S[i]-S[i-1])
    print(*A)
