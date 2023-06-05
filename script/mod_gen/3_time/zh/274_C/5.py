def get_distance(n, a):
    # print("n: ", n)
    # print("a: ", a)
    # print("len(a): ", len(a))
    # print("len(a) * 2 + 1: ", len(a) * 2 + 1)
    distance = [0] * (len(a) * 2 + 1)
    # print("distance: ", distance)
    for i in range(n):
        # print("i: ", i)
        # print("a[i]: ", a[i])
        # print("distance[a[i]]: ", distance[a[i]])
        distance[a[i]] = 0
        # print("distance: ", distance)
        # print("a[i] * 2: ", a[i] * 2)
        # print("distance[a[i] * 2]: ", distance[a[i] * 2])
        distance[a[i] * 2] = distance[a[i]] + 1
        # print("distance: ", distance)
        # print("a[i] * 2 + 1: ", a[i] * 2 + 1)
        # print("distance[a[i] * 2 + 1]: ", distance[a[i] * 2 + 1])
        distance[a[i] * 2 + 1] = distance[a[i]] + 1
        # print("distance: ", distance)
    # print("distance: ", distance)
    return distance

if __name__ == '__main__':
    get_distance()