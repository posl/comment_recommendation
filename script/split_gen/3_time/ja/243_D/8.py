def main():
    N,X = map(int,input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            if X%2 == 0:
                X //= 2
            else:
                X = (X-1)//2
        elif S[i] == "L":
            X = 2*X-1
        else:
            X = 2*X
    print(X)
