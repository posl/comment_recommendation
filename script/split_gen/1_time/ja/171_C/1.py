def main():
    n = int(input())
    ans = ''
    while n > 0:
        if n % 26 == 0:
            ans += 'z'
            n = n // 26 - 1
        else:
            ans += chr(ord('a') + n % 26 - 1)
            n = n // 26
    print(ans[::-1])
