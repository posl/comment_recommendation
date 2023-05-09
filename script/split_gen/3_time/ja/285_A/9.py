def main():
    a, b = map(int, input().split())
    if a + 1 == b or a - 1 == b or a + 3 == b or a - 3 == b or a + 4 == b or a - 4 == b:
        print("Yes")
    else:
        print("No")
