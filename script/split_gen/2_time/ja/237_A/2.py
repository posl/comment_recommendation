def main():
    N = int(input())
    if N >= -2147483648 and N < 2147483648:
        print("Yes")
    else:
        print("No")
