def main():
    n = int(input())
    ans = []
    while n > 0:
        if n % 2 == 0:
            n //= 2
            ans.append('B')
        else:
            n -= 1
            ans.append('A')
    print(''.join(ans[::-1]))
main()
