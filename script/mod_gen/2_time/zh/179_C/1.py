def problem179_c():
    n=int(input())
    cnt=0
    for i in range(1,n):
        for j in range(i,n):
            if i*j>=n:
                break
            if n%(i*j)==0:
                cnt+=1
    return cnt

if __name__ == '__main__':
    problem179_c()