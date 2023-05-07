def main():
    #N
    N = int(input())
    #a_1 a_2 a_3 ... a_N
    a = [int(s) for s in input().split()]
    #print(a)
    cnt = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                break
        else:
            cnt += 1
            continue
        break
    print(cnt)

if __name__ == '__main__':
    main()