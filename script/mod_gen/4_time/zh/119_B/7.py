def calcu_yen(x,u):
    if u == 'BTC':
        return x*380000.0
    else:
        return x

if __name__ == '__main__':
    calcu_yen()