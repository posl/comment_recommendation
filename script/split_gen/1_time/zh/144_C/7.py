def main():
    n = int(input())
    x = 1
    y = 1
    while x*y < n:
        if x < y:
            x += 1
        else:
            y += 1
    print(x+y-2)
