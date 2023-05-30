def solution(H):
    if H == 1:
        return 1
    else:
        return 2*solution(H//2)+1
H = int(input())
print(solution(H))
