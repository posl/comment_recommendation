def cal_distance(l):
    total_length = 0
    for a, b in l:
        total_length += a
    half_length = total_length / 2
    half_length -= l[0][0]
    half_length -= l[0][1]
    half_length -= l[1][0]
    half_length -= l[1][1]
    return half_length

if __name__ == '__main__':
    cal_distance()