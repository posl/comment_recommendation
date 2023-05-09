def main():
    n = int(input())
    s = input()
    r = s.count('R')
    w = n - r
    print(min(r, w))
