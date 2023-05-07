def main():
    a, b = map(int, input().split())
    if a <= b <= a + 2:
        print("Yes")
    else:
        print("No")
