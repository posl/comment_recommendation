def main():
    S,K = input().split()
    K = int(K)
    S = sorted(S)
    ans = ''
    while len(S) > 0:
        #print(S)
        #print(ans)
        #print(K)
        #print('---')
        n = len(S)
        for i in range(n):
            if K <= math.factorial(n-1):
                ans += S[i]
                S.pop(i)
                break
            K -= math.factorial(n-1)
    print(ans)
import math
main()
