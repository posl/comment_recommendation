def permute(s, k):
    if len(s) == 1:
        return s
    elif len(s) == 2:
        if k == 1:
            return s
        else:
            return s[::-1]
    else:
        n = len(s)
        fact = 1
        for i in range(1, n):
            fact *= i
        if k <= fact:
            return s[0] + permute(s[1:], k)
        else:
            return s[0] + permute(s[1:], k-fact)
s, k = input().split()
k = int(k)
print(permute(s, k))

if __name__ == '__main__':
    permute()