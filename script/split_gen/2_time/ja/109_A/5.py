def main():
    a, b = list(map(int, input().split()))
    if (a * b) % 2 == 1:
        print("Yes")
    else:
        print("No")
