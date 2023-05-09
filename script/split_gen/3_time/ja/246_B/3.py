def main():
    A, B = map(int, input().split())
    C = (A**2 + B**2)**(1/2)
    print(A/C, B/C)
