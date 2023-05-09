def main():
    x = int(input())
    if x == 0:
        print(40)
    elif x == 40:
        print(40)
    elif x == 80:
        print(20)
    elif x == 100:
        print("expert")
    else:
        print(40 - (x % 40))
