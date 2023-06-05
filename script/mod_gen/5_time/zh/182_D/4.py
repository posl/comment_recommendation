def main():
    n = input()
    a = map(int, raw_input().split())
    max = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > max:
            max = sum
    print max
main()
