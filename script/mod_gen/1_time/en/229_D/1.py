def max_consecutive_x(s, k):
    max_consecutive_x = 0
    consecutive_x = 0
    for i in range(len(s)):
        if s[i] == 'X':
            consecutive_x += 1
        else:
            if k > 0:
                consecutive_x += 1
                k -= 1
            else:
                consecutive_x = 0
        if consecutive_x > max_consecutive_x:
            max_consecutive_x = consecutive_x
    return max_consecutive_x

if __name__ == '__main__':
    max_consecutive_x()