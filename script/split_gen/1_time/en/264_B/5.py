def main():
    r, c = map(int, input().split())
    if r % 2 == c % 2:
        print("black")
    else:
        print("white")
