def main():
    a, b = map(int, input().split())
    sum = a + b
    if sum < 10:
        print("Easy")
    else:
        print("Hard")