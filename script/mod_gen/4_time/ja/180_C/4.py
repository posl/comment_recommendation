def main():
    n = int(input())
    ans = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)
    for i in sorted(ans):
        print(i)
main()

if __name__ == '__main__':
    main()