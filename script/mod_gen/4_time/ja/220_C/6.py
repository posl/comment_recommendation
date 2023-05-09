def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    a_sum = sum(a)
    a_len = len(a)
    if x < a_sum:
        print(1)
        return
    if x == a_sum:
        print(a_len)
        return
    if x % a_sum == 0:
        print(x // a_sum * a_len)
        return
    if x < a_sum * a_len:
        print(x // a_sum * a_len + 1)
        return
    if x == a_sum * a_len:
        print(x // a_sum * a_len)
        return
    if x % a_sum == 0:
        print(x // a_sum * a_len)
        return
    print(x // a_sum * a_len + (x % a_sum == 0) + 1)

if __name__ == '__main__':
    main()