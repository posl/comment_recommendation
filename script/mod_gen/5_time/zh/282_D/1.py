def main():
    n, m = map(int, input().split())
    u = []
    v = []
    for i in range(m):
        u_i, v_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
    print(n)
    print(m)
    print(u)
    print(v)

if __name__ == '__main__':
    main()