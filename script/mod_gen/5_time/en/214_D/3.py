def main():
    n = int(input())
    u = []
    v = []
    w = []
    for i in range(n-1):
        u_i, v_i, w_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
        w.append(w_i)
    print(u)
    print(v)
    print(w)

if __name__ == '__main__':
    main()