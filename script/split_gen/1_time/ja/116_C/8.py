def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(min([sum([abs(H[i] - H[j]) for j in range(N) if i != j]) for i in range(N)]))
