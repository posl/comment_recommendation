def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        i = str(i)
        if i[0] == i[-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()