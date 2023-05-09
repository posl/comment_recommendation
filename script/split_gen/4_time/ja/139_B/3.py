def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(0)
    else:
        print(1)
