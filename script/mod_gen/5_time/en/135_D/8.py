def count_remainder_5(s):
    count = 0
    for i in range(0, len(s)):
        if s[i] == '?':
            count += count_remainder_5(s[:i] + '0' + s[i+1:])
            count += count_remainder_5(s[:i] + '1' + s[i+1:])
            count += count_remainder_5(s[:i] + '2' + s[i+1:])
            count += count_remainder_5(s[:i] + '3' + s[i+1:])
            count += count_remainder_5(s[:i] + '4' + s[i+1:])
            count += count_remainder_5(s[:i] + '5' + s[i+1:])
            count += count_remainder_5(s[:i] + '6' + s[i+1:])
            count += count_remainder_5(s[:i] + '7' + s[i+1:])
            count += count_remainder_5(s[:i] + '8' + s[i+1:])
            count += count_remainder_5(s[:i] + '9' + s[i+1:])
            break
    else:
        if int(s) % 13 == 5:
            count += 1
    return count

if __name__ == '__main__':
    count_remainder_5()