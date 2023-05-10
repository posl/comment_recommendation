def main():
    K = int(input())
    ans = 0
    for i in range(1, K+1):
        ans = int(str(ans) + '2')
        if ans % K == 0:
            print(i)
            exit()
