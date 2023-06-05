def main():
    n = int(raw_input())
    h = map(int, raw_input().split())
    cnt = 0
    for i in range(n):
        flag = True
        for j in range(i):
            if h[i] < h[j]:
                flag = False
                break
        if flag:
            cnt += 1
    print cnt

if __name__ == '__main__':
    main()