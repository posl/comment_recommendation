def main():
    N = int(input())
    S = input()
    if S[0] == '1' or N % 2 == 0:
        print("Takahashi")
    else:
        print("Aoki")
