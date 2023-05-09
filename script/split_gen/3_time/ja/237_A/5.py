def main():
    N = int(input())
    if -2147483648 <= N and N < 2147483648:
        print("Yes")
    else:
        print("No")
