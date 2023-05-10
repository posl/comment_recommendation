def main():
    n,x = map(int,input().split())
    s = input()
    result = x
    for i in range(n):
        if s[i] == 'o':
            result += 1
        elif result > 0:
            result -= 1
    print(result)

if __name__ == '__main__':
    main()