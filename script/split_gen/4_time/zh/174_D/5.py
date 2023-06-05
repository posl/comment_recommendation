def main():
    n = int(input())
    s = input()
    r = s.count("R")
    w = s.count("W")
    if r == 0 or w == 0:
        print(0)
        return
    if r == w:
        print(r)
        return
    if r > w:
        print(w)
        return
    if r < w:
        print(r)
        return
