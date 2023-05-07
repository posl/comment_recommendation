def count_slimes(s):
    count = 1
    prev = s[0]
    for c in s[1:]:
        if c != prev:
            count += 1
            prev = c
    return count

if __name__ == '__main__':
    count_slimes()