def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [0] * k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    count = 0
    for i in range(n):
        flag = True
        for j in range(k):
            if i+1 not in a[j]:
                flag = False
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()