def main():
    N = int(input())
    A = list(map(int, input().split()))
    subordinates = [0] * N
    for a in A:
        subordinates[a-1] += 1
    for s in subordinates:
        print(s)
