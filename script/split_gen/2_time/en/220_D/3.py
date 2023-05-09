def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * 10
    for a in A:
        count[a] += 1
    for i in range(1, N):
        new_count = [0] * 10
        for j in range(10):
            for k in range(10):
                new_count[(j + k) % 10] += count[j] * count[k]
                new_count[(j * k) % 10] += count[j] * count[k]
        count = new_count
    print("
".join(map(str, count)))
