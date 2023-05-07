def main():
    n = int(input())
    print("Yes" if -2**31 <= n < 2**31 else "No")
