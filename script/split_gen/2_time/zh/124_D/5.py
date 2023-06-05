def solution(s):
    s = s.strip()
    if len(s) == 1:
        return 0
    else:
        count = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
        return count
