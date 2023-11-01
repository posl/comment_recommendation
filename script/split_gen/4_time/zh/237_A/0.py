def main():
    n = int(input())
    if -2**31 <= n <= 2**31 - 1:
        print("Yes")
    else:
        print("No")
