def main():
    N = int(input())
    #N = 14
    #print(N)
    S = ''
    while N > 0:
        if N % 2 == 0:
            S = 'B' + S
            N = int(N/2)
        else:
            S = 'A' + S
            N = N - 1
    print(S)
