def get_count():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    count = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            count += 1
    return count

if __name__ == '__main__':
    get_count()