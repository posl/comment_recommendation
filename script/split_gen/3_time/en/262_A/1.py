def main():
    year = int(input())
    while True:
        if year % 4 == 2:
            print(year)
            break
        else:
            year += 1
