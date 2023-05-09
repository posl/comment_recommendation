def main():
    h,w = map(int,input().split())
    matrix = []
    for i in range(h):
        matrix.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if matrix[j][i] == "#":
                count += 1
        print(count)
