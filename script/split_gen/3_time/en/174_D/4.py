def main():
    n = int(input())
    c = input()
    red = c.count("R")
    white = c.count("W")
    if red == 0 or white == 0:
        print(0)
        return
    if c[0] == "R":
        print(white)
        return
    if c[-1] == "W":
        print(red)
        return
    print(min(red, white))
