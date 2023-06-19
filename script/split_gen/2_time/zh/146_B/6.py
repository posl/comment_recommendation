def problem146_b():
    n = int(input())
    s = input()
    ans = ''
    for c in s:
        ans += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
    print(ans)
