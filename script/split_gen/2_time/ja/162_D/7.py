def main():
    N = int(input())
    S = input()
    print(N*(N-1)*(N-2)//6 - S.count('R')*S.count('G')*S.count('B') - sum((S[i] != S[j]) * (S[j] != S[k]) * (S[k] != S[i]) * (k-j) * (j-i) for i in range(N) for j in range(i+1, N) for k in range(j+1, N)))
