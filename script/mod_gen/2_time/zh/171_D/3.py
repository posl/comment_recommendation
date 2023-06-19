def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    q = int(input())
    bc_list = [list(map(int, input().split())) for _ in range(q)]
    sum_a = sum(a_list)
    d = {}
    for a in a_list:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    for b, c in bc_list:
        if b in d:
            sum_a += (c - b) * d[b]
            if c in d:
                d[c] += d[b]
            else:
                d[c] = d[b]
            d.pop(b)
        print(sum_a)

if __name__ == '__main__':
    main()