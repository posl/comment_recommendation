def main():
    N = input()
    N = int(N)
    S = 0
    for i in str(N):
        S += int(i)
    if N % S == 0:
        print("Yes")
    else:
        print("No")
