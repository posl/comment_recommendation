def main():
    X = int(input())
    if X % 100 == 0:
        print(0)
    else:
        print(100 - X % 100)
