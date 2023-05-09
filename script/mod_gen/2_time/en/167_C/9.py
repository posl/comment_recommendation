def  main():
     #Input
     N, M, X = map(int, input().split())
     C = []
     A = []
     for  i  in  range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
     #Process
     ans = 10 ** 10
     for  i  in  range(1 << N):
        cost = 0
        level = [0] * M
        for  j  in  range(N):
            if  i >> j & 1:
                cost += C[j]
                for  k  in  range(M):
                    level[k] += A[j][k]
         #Output
         if  min(level) >= X:
            ans = min(ans, cost)
     print( -1  if  ans == 10 ** 10  else  ans)

if __name__ == '__main__':
    ()