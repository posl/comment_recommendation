def odd_number_count():
    input()
    return len(list(filter(lambda x: x%2 == 1, map(int, input().split()))))

if __name__ == '__main__':
    odd_number_count()