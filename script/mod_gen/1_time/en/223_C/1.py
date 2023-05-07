def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_sum = sum(a)
    b_sum = sum(b)
    print(a_sum * 1.0 / b_sum)

if __name__ == '__main__':
    main()