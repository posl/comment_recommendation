def main():
    A, B, C = map(int, input().split())
    print("Takahashi" if A > B or C == 0 else "Aoki")
