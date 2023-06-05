def main():
    n, x = map(int, input().split())
    s = input()
    count = 0
    for i in range(n):
        if s[i] == 'o':
            count += 1
        else:
            if count > 0:
                count -= 1
    print(x + count)
main()
