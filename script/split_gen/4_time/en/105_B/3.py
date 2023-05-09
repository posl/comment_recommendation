def main():
    n = int(input())
    if n % 7 == 0 or n % 4 == 0:
        print("Yes")
        return
    for i in range(1, n // 7 + 1):
        if (n - 7 * i) % 4 == 0:
            print("Yes")
            return
    print("No")
