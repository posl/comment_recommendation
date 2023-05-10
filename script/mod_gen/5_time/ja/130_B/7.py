def main():
    n, x = map(int, input().split())
    l_list = list(map(int, input().split()))
    cnt = 1
    d = 0
    for l in l_list:
        d += l
        if d <= x:
            cnt += 1
        else:
            break
    print(cnt)

if __name__ == '__main__':
    main()