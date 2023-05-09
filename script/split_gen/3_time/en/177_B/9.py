def find_min_changes(S, T):
    # Write your code here
    if len(T) > len(S):
        return -1
    min_changes = len(T)
    for i in range(len(S) - len(T) + 1):
        changes = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                changes += 1
        min_changes = min(min_changes, changes)
    return min_changes
