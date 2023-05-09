def main():
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        for j in range(i,N+1):
            if i*j > N:
                break
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()