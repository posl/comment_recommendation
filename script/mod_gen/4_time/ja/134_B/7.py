def get_input_ints():
    return list(map(int, input().split()))
N, D = get_input_ints()
print((N + 2 * D) // (2 * D + 1))

if __name__ == '__main__':
    get_input_ints()