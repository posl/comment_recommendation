def solution(N):
    count = 0
    for i in range(1,N+1):
        if i < 10:
            if i % 2 == 1:
                count += 1
        else:
            if i % 2 == 1:
                count += 1
            else:
                for j in range(1,len(str(i))):
                    if int(str(i)[j]) % 2 == 1:
                        count += 1
                        break
    return count

if __name__ == '__main__':
    solution()