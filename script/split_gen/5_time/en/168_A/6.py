def main():
    n = int(input())
    if n%10 == 3:
        print("bon")
    elif n%10 in [2,4,5,7,9]:
        print("hon")
    else:
        print("pon")
