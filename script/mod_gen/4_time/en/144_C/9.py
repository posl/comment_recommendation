def solution(n):
    i = 1
    j = 1
    count = 0
    while i*j < n:
        if i*j*2 < n:
            if i < j:
                i += 1
            else:
                j += 1
        else:
            if i < j:
                j += 1
            else:
                i += 1
        count += 1
    return count
print(solution(10))
print(solution(50))
print(solution(10000000019))

if __name__ == '__main__':
    solution()