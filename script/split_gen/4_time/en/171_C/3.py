def main():
    n = int(input())
    n -= 1
    ans = []
    while n > -1:
        ans.append(chr(ord('a') + n % 26))
        n //= 26
        n -= 1
    print(''.join(ans[::-1]))
