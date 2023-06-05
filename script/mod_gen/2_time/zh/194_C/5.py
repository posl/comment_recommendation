def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_time = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                min_time = min(min_time, max(a[i], b[j]))
    print(min_time)

if __name__ == '__main__':
    main()