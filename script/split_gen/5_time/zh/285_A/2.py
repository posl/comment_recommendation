def main():
    a, b = map(int, input().split())
    if (a + b) % 3 == 0:
        print("Yes")
    else:
        print("No")
