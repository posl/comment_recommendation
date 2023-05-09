def main():
    a, b = map(int, input().split())
    if b-a == 1 or b-a == 3 or b-a == 5 or b-a == 7 or b-a == 9:
        print("Yes")
    else:
        print("No")
