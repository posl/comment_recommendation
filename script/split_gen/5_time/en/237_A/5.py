def main():
    num = int(input())
    if num >= -2**31 and num <= 2**31-1:
        print("Yes")
    else:
        print("No")
