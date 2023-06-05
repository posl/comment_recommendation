def sort_by_city_and_score(data):
    data.sort(key=lambda x: x[0])
    data.sort(key=lambda x: x[1], reverse=True)
    return data

if __name__ == '__main__':
    sort_by_city_and_score()