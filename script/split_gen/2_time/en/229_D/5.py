def main():
    s = input()
    k = int(input())
    # Count consecutive Xs
    c = 0
    max_c = 0
    for i in range(len(s)):
        if s[i] == 'X':
            c += 1
        else:
            if max_c < c:
                max_c = c
            c = 0
    if max_c < c:
        max_c = c
    # Replace . with X
    if k > 0:
        # Count consecutive Xs after the first X
        c = 0
        for i in range(len(s)):
            if s[i] == 'X':
                c += 1
            else:
                break
        # Count consecutive Xs before the last X
        c2 = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'X':
                c2 += 1
            else:
                break
        # Count consecutive Xs between the first and last X
        c3 = 0
        for i in range(c, len(s) - c2):
            if s[i] == 'X':
                c3 += 1
            else:
                if max_c < c + k:
                    max_c = c + k
                c = 0
        if max_c < c + k:
            max_c = c + k
    print(max_c)
