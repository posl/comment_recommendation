def main():
    K = int(input())
    i = 1
    for i in range(1,K+1):
        if (int(str(7)*i))%K == 0:
            print(i)
            break
        elif i == K:
            print(-1)
            break

if __name__ == '__main__':
    main()