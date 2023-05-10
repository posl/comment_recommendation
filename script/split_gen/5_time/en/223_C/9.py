def main():
    N = int(input())
    A_B = []
    for i in range(N):
        A_B.append(list(map(int,input().split())))
    #print(A_B)
    A_B.sort(key=lambda x:x[0])
    #print(A_B)
    total_time = 0
    for i in range(N):
        total_time += A_B[i][0]/A_B[i][1]
    #print(total_time)
    half_time = total_time/2
    #print(half_time)
    distance = 0
    for i in range(N):
        if half_time <= A_B[i][0]/A_B[i][1]:
            distance += half_time*A_B[i][1]
            break
        else:
            distance += A_B[i][0]
            half_time -= A_B[i][0]/A_B[i][1]
    print(distance)
