def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    p = [[0, 0]]
    for i in range(N):
        if i % 2 == 0:
            p.append([p[i][0] + A[i], p[i][1]])
        else:
            p.append([p[i][0], p[i][1] + A[i]])
    p.append([x, y])
    for i in range(N):
        if p[i][0] == p[i+1][0] == p[i+2][0]:
            if not (p[i][1] < p[i+1][1] < p[i+2][1] or p[i][1] > p[i+1][1] > p[i+2][1]):
                print("No")
                return
        elif p[i][1] == p[i+1][1] == p[i+2][1]:
            if not (p[i][0] < p[i+1][0] < p[i+2][0] or p[i][0] > p[i+1][0] > p[i+2][0]):
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")
    return
main()

if __name__ == '__main__':
    main()