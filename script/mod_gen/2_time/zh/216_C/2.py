def main():
    n = int(input())
    ans = []
    while n > 0:
        if n % 2 == 0:
            ans.append("B")
            n //= 2
        else:
            ans.append("A")
            n -= 1
    ans.reverse()
    print("".join(ans))

if __name__ == '__main__':
    main()