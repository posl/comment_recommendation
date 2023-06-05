def solution(h):
    count = 1
    for i in range(1, len(h)):
        if h[i] >= max(h[:i]):
            count += 1
    return count
