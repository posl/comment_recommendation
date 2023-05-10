def get_hon_pon_bon(n):
    if n % 10 in [2, 4, 5, 7, 9]:
        return 'hon'
    elif n % 10 in [0, 1, 6, 8]:
        return 'pon'
    elif n % 10 == 3:
        return 'bon'
    else:
        return 'error'

if __name__ == '__main__':
    get_hon_pon_bon()