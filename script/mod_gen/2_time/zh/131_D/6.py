def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    c = sorted(zip(a, b), key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += c[i][0]
        if t > c[i][1]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()