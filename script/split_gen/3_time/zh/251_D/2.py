def main():
    w = int(input())
    if w < 3:
        print(1)
        print(w)
    else:
        print(2)
        print(w // 2, w - w // 2)
