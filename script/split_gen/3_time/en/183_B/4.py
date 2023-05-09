def main():
    # read the input
    S_x, S_y, G_x, G_y = map(int, input().split())
    # calculate the result
    result = S_x * G_y / (S_y + G_y)
    # print the result
    print(result)
