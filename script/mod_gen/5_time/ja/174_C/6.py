def main():
    K = int(input())
    ans = -1
    for i in range(1, K+1):
        if int("7"*i) % K == 0:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()