def main():
    n = int(input())
    r = n % 10
    if r == 3:
        print("bon")
    elif r == 0 or r == 1 or r == 6 or r == 8:
        print("pon")
    else:
        print("hon")
