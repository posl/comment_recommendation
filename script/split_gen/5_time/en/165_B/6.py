def main():
    x = int(input())
    y = 100
    year = 0
    while y < x:
        y = y * 1.01
        year += 1
    print(year)
