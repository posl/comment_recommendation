def main():
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        i_str = str(i)
        if i_str[0] == i_str[-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()