def main():
    A, B = map(int, input().split())
    print(B-A+1 if B-A+1 > 0 else 0)
