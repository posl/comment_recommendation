def main():
    #n, x = map(int, input().split())
    #s = input()
    n, x = 20, 10
    s = 'xxxxxxxxxxxxxxxxxxxx'
    s = list(s)
    sum = x
    for i in range(n):
        if s[i] == 'o':
            sum += 1
        elif s[i] == 'x':
            if sum > 0:
                sum -= 1
    print(sum)

if __name__ == '__main__':
    main()