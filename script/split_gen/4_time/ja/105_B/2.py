def main():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0:
        print("Yes")
        return
    for i in range(1, n // 4 + 1):
        if (n - 4 * i) % 7 == 0:
            print("Yes")
            return
    print("No")
