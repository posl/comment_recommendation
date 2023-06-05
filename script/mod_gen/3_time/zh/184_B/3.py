def main():
    n, x = map(int, input().split())
    s = input()
    sum = x
    for i in range(n):
        if s[i] == 'o':
            sum += 1
        elif s[i] == 'x' and sum > 0:
            sum -= 1
    print(sum)

if __name__ == '__main__':
    main()