def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 0:
            a = str(i)[:len(str(i))//2]
            b = str(i)[len(str(i))//2:]
            if a == b:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()