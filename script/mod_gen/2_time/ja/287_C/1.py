def main():
    N, M = map(int, input().split())
    u = []
    v = []
    for i in range(M):
        u_i, v_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
    
    if N - 1 == M:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()