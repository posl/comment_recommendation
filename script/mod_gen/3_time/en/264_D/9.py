def count_swaps(s):
    if len(s) < 2:
        return 0
    if len(s) == 2:
        if s[0] == 'a':
            if s[1] == 't':
                return 0
            else:
                return 1
        else:
            return 2
    if s[0] == 'a':
        return count_swaps(s[1:])
    else:
        return 1 + count_swaps(s[1:])
s = input()
print(count_swaps(s))

if __name__ == '__main__':
    count_swaps()