def war_or_peace(N, M, X, Y, x_list, y_list):
    for i in range(N):
        if x_list[i] >= Y:
            return "War"
    for i in range(M):
        if y_list[i] < X:
            return "War"
    return "No War"

if __name__ == '__main__':
    war_or_peace()