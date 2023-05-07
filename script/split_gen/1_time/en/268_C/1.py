def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    happy = [0] * N
    for i in range(N):
        happy[(i - 1) % N] += 1
        happy[i] += 1
        happy[(i + 1) % N] += 1
    happy_count = 0
    for i in range(N):
        if happy[P[i]] > 0:
            happy_count += 1
    print(happy_count)
