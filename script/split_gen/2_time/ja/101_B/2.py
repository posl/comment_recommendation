def main():
    N = int(input())
    S = 0
    for n in str(N):
        S += int(n)
    if N % S == 0:
        print("Yes")
    else:
        print("No")
