def main():
    N = int(input())
    cnt = 0
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            if i == N//i:
                cnt += i-1
            else:
                cnt += N//i-1
    print(cnt)

if __name__ == '__main__':
    main()