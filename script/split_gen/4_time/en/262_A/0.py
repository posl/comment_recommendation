def main():
    year = int(input())
    while True:
        year += 1
        if year % 4 == 2:
            print(year)
            break
