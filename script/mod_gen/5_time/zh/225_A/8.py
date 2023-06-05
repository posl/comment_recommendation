def solution():
    s = input()
    a = s[0]
    b = s[1]
    c = s[2]
    if a == b == c:
        print(1)
    elif a == b or a == c or b == c:
        print(3)
    else:
        print(6)

if __name__ == '__main__':
    solution()