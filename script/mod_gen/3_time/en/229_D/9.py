def main():
    s = input()
    k = int(input())
    n = len(s)
    s += '.'
    # Find the maximum number of consecutive Xs
    # in the string by replacing at most K dots.
    max_x = 0
    for i in range(n):
        if s[i] == '.':
            j = i + 1
            while s[j] == '.':
                j += 1
            max_x = max(max_x, j - i)
    # Find the maximum number of consecutive Xs
    # in the string by replacing at most K dots.
    max_x = 0
    for i in range(n):
        if s[i] == '.':
            j = i + 1
            while s[j] == '.':
                j += 1
            max_x = max(max_x, j - i)
    # If K is greater than or equal to the number of dots,
    # we can replace all dots with Xs.
    if k >= s.count('.'):
        print(n)
        return
    # If there is a dot in the string,
    # we can replace all dots with Xs.
    if s.count('.') > 0:
        print(n)
        return
    # If there is no dot in the string,
    # we cannot replace any dots with Xs.
    print(max_x)

if __name__ == '__main__':
    main()