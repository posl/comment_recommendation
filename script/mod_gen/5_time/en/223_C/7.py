def main():
    import sys
    import math
    n = int(input())
    a_b = []
    for i in range(n):
        a_b.append(list(map(int, input().split())))
    a_b.sort(key=lambda x: x[0])
    a_b.sort(key=lambda x: x[1], reverse=True)
    a = [x[0] for x in a_b]
    b = [x[1] for x in a_b]
    sum_a = sum(a)
    sum_b = sum(b)
    sum_a_b = 0
    for i in range(n):
        sum_a_b += a[i]
        sum_b -= b[i]
        if sum_a_b > sum_b:
            print(sum_a_b - a[i] + (sum_b - (sum_a_b - a[i]))/2)
            sys.exit()

if __name__ == '__main__':
    main()