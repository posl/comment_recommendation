def main():
    num = int(input())
    if num % 10 == 2 or num % 10 == 4 or num % 10 == 5 or num % 10 == 7 or num % 10 == 9:
        print("hon")
    elif num % 10 == 0 or num % 10 == 1 or num % 10 == 6 or num % 10 == 8:
        print("pon")
    elif num % 10 == 3:
        print("bon")
