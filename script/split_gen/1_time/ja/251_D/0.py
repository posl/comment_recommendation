def main():
    w = int(input())
    if w % 2 == 0 and w > 2:
        print(2)
        print(w//2, w//2)
    else:
        print(3)
        print(1, 2, w-3)
