def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)
    a_sum = sum(a)
    count = []
    for i in range(q):
        count.append(a.count(b[i]))
        a_sum += (c[i] - b[i]) * count[i]
        print(a_sum)

if __name__ == '__main__':
    main()