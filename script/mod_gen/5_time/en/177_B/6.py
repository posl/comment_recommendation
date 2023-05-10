def find_min_changes(s, t):
    min_changes = len(s)
    for i in range(len(s) - len(t) + 1):
        changes = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                changes += 1
        if changes < min_changes:
            min_changes = changes
    return min_changes

if __name__ == '__main__':
    find_min_changes()