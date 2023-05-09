def S(n):
    return sum([int(i) for i in str(n)])
a, b = map(int, input().split())
print(max(S(a), S(b)))

if __name__ == '__main__':
    S()