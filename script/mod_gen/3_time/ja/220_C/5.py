def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum_a = sum(a)
    k = 0
    for _ in range(100):
        k += n
        if sum_a * k > x:
            break
    for i in range(n):
        k += 1
        if sum_a * k > x:
            break
    print(k)

if __name__ == '__main__':
    main()