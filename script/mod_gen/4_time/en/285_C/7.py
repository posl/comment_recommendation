def solution():
    s = input()
    order = 0
    for i in range(len(s)):
        order = order * 26 + (ord(s[i]) - ord('A') + 1)
    print(order)
solution()

if __name__ == '__main__':
    solution()