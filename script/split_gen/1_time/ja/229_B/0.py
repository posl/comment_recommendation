def main():
    A, B = map(int, input().split())
    if A + B < 10 ** 19:
        print("Easy")
    else:
        print("Hard")
