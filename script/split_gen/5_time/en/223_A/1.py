def main():
    x = int(input())
    if x < 100:
        print("No")
    elif x % 100 == 0:
        print("Yes")
    else:
        print("No")
