def get_candies(N, K, candies):
    candies = candies.split()
    candies = [int(x) for x in candies]
    candies = set(candies)
    if len(candies) <= K:
        return len(candies)
    else:
        return K

if __name__ == '__main__':
    get_candies()