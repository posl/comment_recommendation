def move(s, n):
    # print(s)
    # print(n)
    # print(ord('A'))
    # print(ord('Z'))
    # print(ord('a'))
    # print(ord('z'))
    # print(ord(s))
    # print(ord(s) + n)
    # print(ord(s) + n - ord('A'))
    # print(ord(s) + n - ord('A') % 26)
    # print((ord(s) + n - ord('A')) % 26)
    # print(chr(ord(s) + n - ord('A') % 26))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    if ord(s) >= ord('A') and ord(s) <= ord('Z'):
        return chr((ord(s) + n - ord('A')) % 26 + ord('A'))
    elif ord(s) >= ord('a') and ord(s) <= ord('z'):
        return chr((ord(s) + n - ord('a')) % 26 + ord('a'))
    else:
        return s
n = int(input())
s = input()
# print(move('A', 2))
# print(move('Y', 3))
# print(move('A', 0))
# print(move('A', 26))
# print(move('A', 27))
# print(move('a', 2))
# print(move('y', 3))
# print(move('a', 0
