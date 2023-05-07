def main():
    n = int(input())
    v = list(map(int, input().split()))
    a = [0] * (10**5 + 1)
    b = [0] * (10**5 + 1)
    for i in range(n):
        if i % 2 == 0:
            a[v[i]] += 1
        else:
            b[v[i]] += 1
    a_max = max(a)
    b_max = max(b)
    a_max_i = a.index(a_max)
    b_max_i = b.index(b_max)
    if a_max_i != b_max_i:
        print(n - a_max - b_max)
    else:
        a.sort(reverse=True)
        b.sort(reverse=True)
        print(n - max(a[0] + b[1], a[1] + b[0]))

if __name__ == '__main__':
    main()