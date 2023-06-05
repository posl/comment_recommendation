def main():
    N,K = map(int,input().split())
    S = input()
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    happy += 2*K
    print(min(happy,N-1))
main()
