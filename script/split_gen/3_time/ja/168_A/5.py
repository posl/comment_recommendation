def main():
    n = int(input())
    l = n % 10
    if l == 2 or l == 4 or l == 5 or l == 7 or l == 9:
        print("hon")
    elif l == 0 or l == 1 or l == 6 or l == 8:
        print("pon")
    elif l == 3:
        print("bon")
