def main():
    X = int(input())
    for A in range(1, 1000):
        for B in range(1, 1000):
            if A ** 5 - B ** 5 == X:
                print(A, B)
                return
