def main():
    Y = int(input())
    while Y < 2000 or Y > 3000:
        Y = int(input())
    while (Y % 4) != 2:
        Y += 1
    print(Y)
