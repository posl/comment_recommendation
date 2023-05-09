def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    if n < 0:
        n = -n
        sign = -1
    else:
        sign = 1
    ans = ''
    while n > 0:
        ans += str(n % 2)
        n //= 2
    if sign == -1:
        ans = ans.replace('0', 'a')
        ans = ans.replace('1', '0')
        ans = ans.replace('a', '1')
    print(ans[::-1])
