def triangle_count(n, lines):
    lines.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if lines[i] + lines[j] > lines[k]:
                    count += 1
    return count
