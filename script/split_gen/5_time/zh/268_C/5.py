def main():
    N = int(input())
    p = list(map(int, input().split()))
    max = 0
    happy = 0
    for i in range(N):
        if p[i] == i:
            happy += 1
            if happy > max:
                max = happy
        else:
            happy = 0
    print(max)
