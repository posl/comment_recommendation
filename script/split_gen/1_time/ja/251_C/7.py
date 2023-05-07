def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    max_point = -1
    max_point_index = -1
    for i in range(N):
        if T[i] > max_point:
            max_point = T[i]
            max_point_index = i
    max_point_count = 0
    for i in range(N):
        if T[i] == max_point:
            max_point_count += 1
    if max_point_count == 1:
        print(max_point_index+1)
        return
    for i in range(N):
        if T[i] == max_point:
            for j in range(i):
                if S[i] == S[j]:
                    max_point_count -= 1
                    break
    if max_point_count == 1:
        for i in range(N):
            if T[i] == max_point:
                for j in range(i):
                    if S[i] == S[j]:
                        print(j+1)
                        return
    else:
        for i in range(N):
            if T[i] == max_point:
                print(i+1)
                return
