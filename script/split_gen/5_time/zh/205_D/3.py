def main():
    n, q = map(int, input().split())
    numbers = list(map(int, input().split()))
    queries = [int(input()) for _ in range(q)]
    for i in range(q):
        k = queries[i]
        count = 0
        for j in range(n):
            if numbers[j] > count + k:
                print(count + k)
                break
            else:
                count += 1
