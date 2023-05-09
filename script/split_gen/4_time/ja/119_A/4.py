def main():
    s = input()
    y, m, d = map(int, s.split("/"))
    if y < 2019:
        print("Heisei")
    elif y == 2019 and m < 4:
        print("Heisei")
    elif y == 2019 and m == 4 and d <= 30:
        print("Heisei")
    else:
        print("TBD")
