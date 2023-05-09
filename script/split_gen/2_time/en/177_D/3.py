def main():
    n, m = map(int, input().split())
    friends = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a - 1].add(b - 1)
        friends[b - 1].add(a - 1)
    groups = [None] * n
    group_count = 0
    for i in range(n):
        if groups[i] is not None:
            continue
        groups[i] = group_count
        stack = [i]
        while stack:
            p = stack.pop()
            for q in friends[p]:
                if groups[q] is None:
                    groups[q] = group_count
                    stack.append(q)
        group_count += 1
    print(group_count)
main()
