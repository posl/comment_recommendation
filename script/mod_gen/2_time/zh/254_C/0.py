def pascal_triangle(n):
    """打印帕斯卡三角形"""
    row = [1]
    yh = []
    for i in range(n):
        yh.append(row)
        row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
    return yh

if __name__ == '__main__':
    pascal_triangle()