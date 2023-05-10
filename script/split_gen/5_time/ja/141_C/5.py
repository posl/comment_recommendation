def main():
    n, k, q = map(int, input().split())
    score = [k] * n
    for _ in range(q):
        a = int(input())
        score[a-1] += 1
    for i in range(n):
        if score[i] > q:
            print("Yes")
        else:
            print("No")
