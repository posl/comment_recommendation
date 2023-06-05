def main():
    N = int(input())
    p = list(map(int, input().split()))
    p2 = list(map(lambda x: x-1, p))
    happy = 0
    for i in range(N):
        if p2[p2[i]] == i:
            happy += 1
    print(happy)
main()
