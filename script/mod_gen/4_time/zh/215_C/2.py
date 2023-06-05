def getPermutation(s, k):
    if len(s) == 1:
        return s
    else:
        char_list = list(s)
        char_list.sort()
        next_str = ''.join(char_list[1:])
        num = 1
        for i in range(1, len(s)):
            num *= i
        index = (k - 1) / num
        return char_list[index] + getPermutation(next_str, k - index * num)

if __name__ == '__main__':
    getPermutation()