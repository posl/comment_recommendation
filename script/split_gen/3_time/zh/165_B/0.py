def main():
    x = int(input())
    s = 100
    y = 0
    while x > s:
        s = s + s//100
        y += 1
    print(y)
