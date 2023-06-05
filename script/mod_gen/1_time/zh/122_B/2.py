def solution():
    s = input()
    n = len(s)
    max = 0
    for i in range(n):
        for j in range(i, n):
            if check(s[i:j + 1]):
                if max < j - i + 1:
                    max = j - i + 1
    print(max)

if __name__ == '__main__':
    solution()