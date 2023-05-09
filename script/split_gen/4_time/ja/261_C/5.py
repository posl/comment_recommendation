def main():
    n = int(input())
    s = [input() for _ in range(n)]
    memo = {}
    for i in range(n):
        if s[i] in memo:
            memo[s[i]] += 1
            print(s[i] + '(' + str(memo[s[i]] - 1) + ')')
        else:
            memo[s[i]] = 1
            print(s[i])
