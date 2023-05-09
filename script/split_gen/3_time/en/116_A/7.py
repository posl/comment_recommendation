def main():
    # get the input
    ab, bc, ca = map(int, input().split())
    # get the area of the triangle
    area = (ab * bc) // 2
    # print the area
    print(area)
