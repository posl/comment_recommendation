def get_paths(start, cities, visited, total, k):
    if len(visited) == len(cities):
        if start in cities:
            total += cities[start]
            if total == k:
                return 1
            else:
                return 0
    else:
        total += cities[start]
        visited.append(start)
        for city in cities:
            if city not in visited:
                return get_paths(city, cities, visited, total, k)
    return 0

if __name__ == '__main__':
    get_paths()