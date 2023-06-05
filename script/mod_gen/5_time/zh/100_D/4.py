def get_max_value(n,m,beauty,delicious,popularity):
    max_value = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                value = abs(beauty[i])+abs(beauty[j])+abs(beauty[k])+abs(delicious[i])+abs(delicious[j])+abs(delicious[k])+abs(popularity[i])+abs(popularity[j])+abs(popularity[k])
                if value > max_value:
                    max_value = value
    return max_value

if __name__ == '__main__':
    get_max_value()