def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b_c = list(map(int, input().split()))
        b.append(b_c[0])
        c.append(b_c[1])
    a_sum = sum(a)
    for i in range(q):
        a_sum += (c[i] - b[i]) * a.count(b[i])
        print(a_sum)
        a_sum -= (c[i] - b[i]) * a.count(b[i])
        a = [c[i] if x == b[i] else x for x in a]

if __name__ == '__main__':
    main()