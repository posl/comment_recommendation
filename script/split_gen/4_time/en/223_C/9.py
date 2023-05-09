def main():
    n = int(input())
    a_b = []
    for i in range(n):
        a_b.append(input().split(' '))
    a_b = [[int(a_b[i][0]), int(a_b[i][1])] for i in range(n)]
    a_b = sorted(a_b, key=lambda x: x[0])
    time = 0
    for i in range(n):
        time += a_b[i][0] / a_b[i][1]
    half_time = time / 2
    distance = 0
    for i in range(n):
        if half_time > a_b[i][0] / a_b[i][1]:
            half_time -= a_b[i][0] / a_b[i][1]
            distance += a_b[i][0]
        else:
            distance += half_time * a_b[i][1]
            break
    print(distance)
