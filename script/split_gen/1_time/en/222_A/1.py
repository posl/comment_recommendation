def main():
    num = input()
    if len(num) == 1:
        print("000" + num)
    elif len(num) == 2:
        print("00" + num)
    elif len(num) == 3:
        print("0" + num)
    else:
        print(num)
