def get_generation_distance(n, a):
    generation_distance = [0 for i in range(2*n+1)]
    generation_distance[1] = 0
    for i in range(n):
        generation_distance[2*(i+1)] = generation_distance[a[i]] + 1
        generation_distance[2*(i+1)+1] = generation_distance[a[i]] + 1
    return generation_distance

if __name__ == '__main__':
    get_generation_distance()