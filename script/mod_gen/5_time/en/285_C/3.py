def base26_to_int(s):
    n = 0
    for c in s:
        n = n*26 + ord(c) - ord('A') + 1
    return n
s = input()
print(base26_to_int(s))

if __name__ == '__main__':
    base26_to_int()