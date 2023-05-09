def main():
    X = int(input())
    for A in range(-1000, 1001):
        for B in range(-1000, 1001):
            if A**5 - B**5 == X:
                print(A, B)
                exit()
