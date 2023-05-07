def main():
    K = int(input())
    ans = 1
    for i in range(2,K+1):
        ans *= i
        if ans%K == 0:
            print(i)
            exit()
    print(K)
