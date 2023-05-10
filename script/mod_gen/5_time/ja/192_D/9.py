def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
X = input()
M = int(input())
d = max([int(x) for x in X])
d = d + 1
l = len(X)

if __name__ == '__main__':
    Base_10_to_n()