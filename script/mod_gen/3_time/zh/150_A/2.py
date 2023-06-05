def is_enough(coin, money):
    if (coin * 500) >= money:
        return True
    else:
        return False

if __name__ == '__main__':
    is_enough()