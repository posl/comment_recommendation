def solution(a,b):
    #a = 8
    #b = 13
    #a = 54
    #b = 65
    sum = 0
    for i in range(1,1000):
        sum = sum + i
        if sum == b - a:
            return i - 1
        if sum > b - a:
            return i - 2

if __name__ == '__main__':
    solution()