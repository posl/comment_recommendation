def solution(x):
    x = str(x)
    if '.' in x:
        return int(float(x)+0.5)
    else:
        return int(x)

if __name__ == '__main__':
    solution()