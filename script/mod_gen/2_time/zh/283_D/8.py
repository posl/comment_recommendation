def solve(s):
    s = list(s)
    s.reverse()
    i = 0
    count = 0
    while i < len(s):
        if s[i] == '0':
            i += 1
            count += 1
        else:
            j = i
            while j < len(s):
                if s[j] == '0':
                    break
                j += 1
            if j == len(s):
                break
            else:
                count += 1
                i = j
    return count

if __name__ == '__main__':
    solve()