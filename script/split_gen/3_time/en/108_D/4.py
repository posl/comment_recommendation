def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(N-1):
        print(i+1, i+2, 0)
    for i in range(N-1):
        print(i+1, i+2, 1)
    for i in range(1, N-1):
        print(1, i+2, i+1)
    for i in range(N-2):
        print(i+2, i+3, 0)
    for i in range(N-2):
        print(i+2, i+3, 1)
    for i in range(1, N-2):
        print(1, i+3, i+2)
    for i in range(N-3):
        print(i+3, i+4, 0)
    for i in range(N-3):
        print(i+3, i+4, 1)
    for i in range(1, N-3):
        print(1, i+4, i+3)
    for i in range(N-4):
        print(i+4, i+5, 0)
    for i in range(N-4):
        print(i+4, i+5, 1)
    for i in range(1, N-4):
        print(1, i+5, i+4)
    for i in range(N-5):
        print(i+5, i+6, 0)
    for i in range(N-5):
        print(i+5, i+6, 1)
    for i in range(1, N-5):
        print(1, i+6, i+5)
    for i in range(N-6):
        print(i+6, i+7, 0)
    for i in range(N-6):
        print(i+6, i+7, 1)
    for i in range(1, N-6):
        print(1, i+7, i+6)
    for i in range(N-7):
        print(i+7, i+8, 0)
    for i in range(N-7):
        print(i+7, i+8, 1)
    for i in range(1, N-7):
        print(1
