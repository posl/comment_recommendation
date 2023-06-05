def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    if r == w:
        print(1)
        return
    if r > w:
        print(w)
    else:
        print(r)
