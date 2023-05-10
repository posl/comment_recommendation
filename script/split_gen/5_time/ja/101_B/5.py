def main():
    N = int(input())
    S = sum([int(i) for i in str(N)])
    if N % S == 0:
        print("Yes")
    else:
        print("No")
