def main():
    A, B, C, D = map(int, input().split())
    while True:
        C -= B
        if C <= 0:
            print("Yes")
            break
        A -= D
