def cal(N,K):
    if K%2 == 0:
        if N%2 == 0:
            return int(N*N*N/K)
        else:
            return int((N-1)*(N-1)*(N-1)/K)
    else:
        return int((N/K)**3)
N,K = map(int,input().split())
print(cal(N,K))

if __name__ == '__main__':
    cal()