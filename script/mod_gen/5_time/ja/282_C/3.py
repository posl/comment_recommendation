def main():
    n = int(input())
    s = input()
    s = list(s)
    k = 0
    for i in range(n):
        if s[i] == '"':
            k += 1
        if s[i] == ',' and k % 2 == 0:
            s[i] = '.'
    print(''.join(s))
main()

if __name__ == '__main__':
    main()