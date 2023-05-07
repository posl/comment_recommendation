def main():
    A, B = map(int, input().split())
    if A <= B:
        print(B-A+1)
    else:
        print(0)
