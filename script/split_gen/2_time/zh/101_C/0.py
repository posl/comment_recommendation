def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if len(set(a)) == 1:
            break
        min_value = min(a)
        min_index = a.index(min_value)
        for i in range(min_index, min_index+k):
            a[i] = min_value
        count += 1
    print(count)
