def main():
    n = int(input())
    n = str(n)
    n = n[::-1]
    if n == n[::-1]:
        print("Yes")
    else:
        print("No")
