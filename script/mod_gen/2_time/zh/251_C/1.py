def get_weights(n,w):
    # n: the number of weights
    # w: the weight limit
    weights = []
    for i in range(n):
        weights.append(int(input()))
    return weights

if __name__ == '__main__':
    get_weights()