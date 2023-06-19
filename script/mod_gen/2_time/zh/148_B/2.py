def main():
    n = int(input())
    s, t = input().split()
    result = []
    for i in range(n):
        result.append(s[i])
        result.append(t[i])
    print(''.join(result))

if __name__ == '__main__':
    main()