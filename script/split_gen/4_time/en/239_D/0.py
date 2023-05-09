def main():
    A, B, C, D = map(int, input().split())
    for i in range(A, B+1):
        for j in range(C, D+1):
            if (i + j) % 2 == 0:
                print("Takahashi")
                return
    print("Aoki")
