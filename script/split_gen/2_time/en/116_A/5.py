def main():
    # read the input
    AB, BC, CA = map(int, input().split())
    # calculate the area
    area = int((AB * BC) / 2)
    # print the area
    print(area)
