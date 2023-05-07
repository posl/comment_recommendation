def main():
    n = int(input())
    print("Yes" if str(n) == str(n)[::-1] else "No")
