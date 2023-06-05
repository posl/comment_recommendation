def solution(h):
    if h == 1:
        return 1
    return solution(h//2)*2+1
