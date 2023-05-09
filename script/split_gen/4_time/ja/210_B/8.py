def main():
    n = int(input())
    s = input()
    print("Takahashi" if s.index('1') % 2 == 0 else "Aoki")
