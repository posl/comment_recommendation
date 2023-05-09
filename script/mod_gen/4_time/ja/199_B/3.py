def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    cnt = 0
    for i in range(1, 1001):
        flag = True
        for j in range(n):
            if not (a[j] <= i <= b[j]):
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()