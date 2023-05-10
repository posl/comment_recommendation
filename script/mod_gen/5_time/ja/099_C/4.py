def get_min_count(n):
    min_count = n
    for i in range(1, int(n**(1/6))+1):
        for j in range(1, int(n**(1/9))+1):
            if n >= 6**i + 9**j:
                count = i + j
                if count < min_count:
                    min_count = count
    return min_count

if __name__ == '__main__':
    get_min_count()