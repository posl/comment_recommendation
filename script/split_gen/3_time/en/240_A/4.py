def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a + 1 == b or a - 1 == b or a + 9 == b or a - 9 == b:
        print("Yes")
    else:
        print("No")
