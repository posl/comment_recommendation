def main():
    A, B, C, D = map(int, input().split())
    prime = [0] * 1000
    for i in range(3, 1000, 2):
        prime[i] = 1
    for i in range(3, 1000, 2):
        if prime[i]:
            for j in range(i * 2, 1000, i):
                prime[j] = 0
    for i in range(A, B + 1):
        for j in range(C, D + 1):
            if prime[i + j] == 1:
                print("Aoki")
                return
    print("Takahashi")
