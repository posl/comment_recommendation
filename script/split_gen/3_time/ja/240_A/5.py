def main():
    a, b = map(int, input().split())
    if a + 1 == b or a - 1 == b or a + 8 == b or a - 8 == b:
        print("Yes")
    else:
        print("No")
