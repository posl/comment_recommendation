def solve(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+3,len(s)+1):
            if int(s[i:j])%2019 == 0:
                count += 1
    return count
