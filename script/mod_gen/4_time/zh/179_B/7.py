def solution():
    count = int(input())
    result = []
    for i in range(count):
        result.append(input().split(' '))
    for i in range(count-2):
        if result[i][0] == result[i][1] and result[i+1][0] == result[i+1][1] and result[i+2][0] == result[i+2][1]:
            print('Yes')
            return
    print('No')
solution()
