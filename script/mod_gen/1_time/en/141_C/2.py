def main():
    n, k, q = map(int, input().split())
    score = [0] * n
    for i in range(q):
        a = int(input())
        score[a-1] += 1
    for i in range(n):
        if k - q + score[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()