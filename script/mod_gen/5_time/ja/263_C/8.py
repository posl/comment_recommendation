def prob_c():
    N,M = map(int, input().split())
    array = [1]*N
    array[0] = 1
    current = 0
    while True:
        if current == N-1:
            print(*array)
            array[current] += 1
            if array[current] > M:
                array[current] = 1
                current -= 1
            continue
        if array[current] > M:
            array[current] = 1
            current -= 1
            continue
        if array[current] >= array[current+1]:
            array[current] += 1
            continue
        if array[current] < array[current+1]:
            current += 1
            continue
        if current == 0:
            break
    return
prob_c()

if __name__ == '__main__':
    prob_c()