def solution(a, b):
    if a == b:
        return "IMPOSIBLE"
    if a > b:
        if (a - b) % 2 == 0:
            return int((a - b) / 2 + b)
        else:
            return "IMPOSIBLE"
    else:
        if (b - a) % 2 == 0:
            return int((b - a) / 2 + a)
        else:
            return "IMPOSIBLE"

if __name__ == '__main__':
    solution()