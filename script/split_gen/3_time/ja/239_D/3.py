def main():
    A, B, C, D = map(int, input().split())
    if B < C or D < A:
        print("Aoki")
    else:
        print("Takahashi")
