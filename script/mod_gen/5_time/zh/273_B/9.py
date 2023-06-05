def solution(x,k):
    for i in range(k):
        x = (x//10+1)*10 if x%10>=5 else (x//10)*10
    return x

if __name__ == '__main__':
    solution()