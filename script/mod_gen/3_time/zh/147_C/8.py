def get_ans(N, A, xy):
    ans = 0
    for i in range(2**N):
        b = [0]*N
        for j in range(N):
            if ((i>>j)&1):
                b[j] = 1
        flag = 1
        for j in range(N):
            if b[j] == 1:
                for k in range(A[j]):
                    if b[xy[j][k][0]-1] != xy[j][k][1]:
                        flag = 0
                        break
                if flag == 0:
                    break
        if flag == 1:
            ans = max(ans, sum(b))
    return ans

if __name__ == '__main__':
    get_ans()