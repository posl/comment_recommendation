def main():
    num = int(input())
    str = input()
    if num % 2 == 0:
        half = int(num / 2)
        if str[0:half] == str[half:]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
