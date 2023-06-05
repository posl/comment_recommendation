def last_card(n, k, a):
    return (k - (n - a + 1)) % n + 1

if __name__ == '__main__':
    last_card()