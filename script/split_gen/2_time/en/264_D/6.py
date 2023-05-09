def main():
    s = input()
    def solve(s):
        if not s:
            return 0
        if s[0] == 'a':
            return solve(s[1:])
        else:
            return 1 + solve(s[1:])
    print(solve(s))
