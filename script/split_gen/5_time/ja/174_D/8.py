def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = n - r
    rw = c[:r].count('W')
    print(rw)
