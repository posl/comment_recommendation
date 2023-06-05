def main():
    n,k = map(int,input().split())
    s = input()
    start = s[0]
    if start == "R":
        s = s[::-1]
    s = s.repl
