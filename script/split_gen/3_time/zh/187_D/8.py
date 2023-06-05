def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort(reverse=True)
    b.sort(reverse=True)
    a_sum = sum(a)
    b_sum = sum(b)
    a_count = 0
    b_count = 0
    for i in range(n):
        a_count += a[i]
        b_count += b[i]
        if a_count > b_count:
            print(i+1)
            break
        elif i == n-1:
            print(n)
main()
