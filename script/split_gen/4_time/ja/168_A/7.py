def main():
    N = int(input())
    last_digit = N % 10
    if last_digit == 2 or last_digit == 4 or last_digit == 5 or last_digit == 7 or last_digit == 9:
        print("hon")
    elif last_digit == 0 or last_digit == 1 or last_digit == 6 or last_digit == 8:
        print("pon")
    else:
        print("bon")
