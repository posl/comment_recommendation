def train(x, y, a, b):
    exp = 0
    while True:
        if x * a < x + b:
            if x * a >= y:
                return exp
            else:
                x *= a
                exp += 1
        else:
            if x + b >= y:
                return exp
            else:
                x += b
                exp += 1

if __name__ == '__main__':
    train()