def main():
    a, b = map(int, input().split())
    if (a + 1) % 10 == b % 10:
        print("Yes")
    else:
        print("No")
