def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a * b > 0:
        if a < b:
            print(a * b)
        else:
            print(a * b)
    else:
        print("0")
