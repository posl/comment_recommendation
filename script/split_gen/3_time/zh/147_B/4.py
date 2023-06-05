def main():
    s = input()
    print(len(s) - sum([1 for i in range(len(s)//2) if s[i] != s[-i-1]]))
