def main():
    # input
    K = int(input())
    A, B = map(int, input().split())
    # compute
    ans = 'NG'
    for i in range(A, B+1):
        if i % K == 0:
            ans = 'OK'
            break
    # output
    print(ans)
