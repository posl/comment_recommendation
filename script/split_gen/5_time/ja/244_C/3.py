def main():
    N = int(input())
    L = 1
    R = 2*N+1
    while True:
        M = (L+R)//2
        print(M)
        S = int(input())
        if S == 0:
            break
        elif S == 1:
            L = M+1
        else:
            R = M-1
