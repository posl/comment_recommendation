def main():
    n = int(input())
    s = input()
    c = s.count('R')
    ans = s[:c].count('W')
    print(ans)
