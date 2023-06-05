def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    sum_a = sum(a)
    for i in range(q):
        print(sum_a + x[i] * n)

if __name__ == '__main__':
    main()