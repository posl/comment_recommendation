def is_star(n, edges):
    if n != len(edges) + 1:
        return False
    if n == 1:
        return True
    if n == 2:
        return False
    if n == 3:
        return True
    count = [0] * (n + 1)
    for e in edges:
        count[e[0]] += 1
        count[e[1]] += 1
    for i in range(1, n + 1):
        if count[i] == n - 1:
            return True
    return False

if __name__ == '__main__':
    is_star()