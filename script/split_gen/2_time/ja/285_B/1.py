def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        for k in range(1,N-i+1):
            if S[k-1] != S[k+i-1]:
                l = k
            else:
                break
        print(l)
