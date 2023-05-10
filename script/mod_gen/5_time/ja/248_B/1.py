def count_scream(a, b, k):
    count = 0
    while a < b:
        a *= k
        count += 1
    return count
a, b, k = map(int, input().split())
print(count_scream(a, b, k))

if __name__ == '__main__':
    count_scream()