def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = input().split()
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    min_time = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                min_time = min(min_time, a[i] + b[j])
            else:
                min_time = min(min_time, max(a[i], b[j]))
    print(min_time)

if __name__ == '__main__':
    main()