def main():
    n = int(input())
    p = list(map(int, input().split()))
    max = 0
    for i in range(n):
        cnt = 0
        j = i
        while j > 0:
            j = p[j - 1]
            cnt += 1
        if cnt > max:
            max = cnt
    print(max)

if __name__ == '__main__':
    main()