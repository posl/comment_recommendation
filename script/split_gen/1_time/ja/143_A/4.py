def main():
    A, B = map(int, input().split())
    if B >= A:
        print(0)
    else:
        print(A - B - B)
