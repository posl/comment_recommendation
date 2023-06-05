def main():
    x = int(input())
    m = 100
    year = 0
    while m < x:
        m = int(m * 1.01)
        year += 1
    print(year)
