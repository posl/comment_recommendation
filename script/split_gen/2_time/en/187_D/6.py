def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    
    c = sorted(c, reverse=True)
    a = sorted(a, reverse=True)
    sum_a = sum(a)
    sum_c = 0
    for i in range(n):
        sum_c += c[i]
        if sum_c > sum_a:
            print(i + 1)
            break
main()
