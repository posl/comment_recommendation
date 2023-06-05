def main():
    N = int(input())
    s, t = input().split()
    result = ''
    for i in range(N):
        result += s[i]
        result += t[i]
    print(result)

if __name__ == '__main__':
    main()