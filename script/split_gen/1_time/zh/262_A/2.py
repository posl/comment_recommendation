def main():
    Y = int(input())
    while Y <= 3000:
        Y += 1
        if Y % 4 == 2:
            break
    print(Y)
