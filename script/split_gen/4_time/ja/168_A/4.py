def main():
    n = int(input())
    hon = [2, 4, 5, 7, 9]
    pon = [0, 1, 6, 8]
    bon = [3]
    if n % 10 in hon:
        print("hon")
    elif n % 10 in pon:
        print("pon")
    else:
        print("bon")
