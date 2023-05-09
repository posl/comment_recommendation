def main():
    r, c = map(int, input().split())
    if r % 2 == 0 and c % 2 == 0:
        print("white")
    elif r % 2 == 0 and c % 2 != 0:
        print("black")
    elif r % 2 != 0 and c % 2 == 0:
        print("black")
    else:
        print("white")
