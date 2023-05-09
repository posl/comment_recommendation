def main():
    N = int(input())
    P = list(map(int, input().split()))
    counter = 0
    for i in range(N):
        if P[i] == min(P[:i+1]):
            counter += 1
    print(counter)
