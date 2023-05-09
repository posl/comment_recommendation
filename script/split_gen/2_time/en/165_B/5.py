def main():
    X = int(input())
    Y = 100
    count = 0
    while Y < X:
        Y = int(Y * 1.01)
        count += 1
    print(count)
