def get_next_city(city, visited_cities):
    for i in range(1, N+1):
        if i not in visited_cities:
            yield i

if __name__ == '__main__':
    get_next_city()