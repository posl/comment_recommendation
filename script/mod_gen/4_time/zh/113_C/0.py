def id_generator(county, year, cities):
    id = ""
    for i in range(1, len(cities[county])+1):
        if cities[county][i] == year:
            id = str(county).zfill(6) + str(i).zfill(6)
            break
    return id

if __name__ == '__main__':
    id_generator()