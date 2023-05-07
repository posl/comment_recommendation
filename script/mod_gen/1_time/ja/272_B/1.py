def main():
    N, M = map(int, input().split())
    people = [0] * N
    for i in range(M):
        k, *x = map(int, input().split())
        for j in range(k):
            people[x[j] - 1] += 1
    for i in range(N):
        if people[i] == 0:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()