def count_integers(a, b):
    count = 0
    for i in range(a, b+1):
        count += 1
    return count
a, b = map(int, input().split())
print(count_integers(a, b))

if __name__ == '__main__':
    count_integers()