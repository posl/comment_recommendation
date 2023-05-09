def main():
    N = int(input())
    v = list(map(int, input().split()))
    v1 = v[0::2]
    v2 = v[1::2]
    m1 = max(set(v1), key=v1.count)
    m2 = max(set(v2), key=v2.count)
    if m1 != m2:
        print(N - v1.count(m1) - v2.count(m2))
    else:
        m1 = max(set(v1), key=v1.count)
        m2 = max(set(v2), key=v2.count)
        print(min(N - v1.count(m1) - v2.count(m2), N - v1.count(m2) - v2.count(m1)))

if __name__ == '__main__':
    main()