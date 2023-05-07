def main():
    N, A, B = map(int, input().split())
    #print(N, A, B)
    S = 0
    for i in range(1, N+1):
        if i%A==0 or i%B==0:
            continue
        else:
            S += i
    print(S)
