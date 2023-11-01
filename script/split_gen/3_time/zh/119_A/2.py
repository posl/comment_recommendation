def main():
    s = input()
    year, month, day = s.split("/")
    if int(year) < 2019:
        print("Heisei")
    elif int(month
