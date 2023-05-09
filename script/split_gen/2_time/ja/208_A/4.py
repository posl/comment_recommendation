def main():
    # A, B = map(int, input().split())
    A, B = 100, 600
    for a in range(1, 7):
        for b in range(1, 7):
            if a + b == B:
                print("Yes")
                return
    print("No")
