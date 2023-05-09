def main():
    n = int(input())
    s, t = input().split(' ')
    result = ''
    for i in range(n):
        result += s[i] + t[i]
    print(result)

if __name__ == '__main__':
    main()