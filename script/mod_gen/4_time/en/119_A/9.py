def is_heisei(s):
    if s <= '2019/04/30':
        return 'Heisei'
    else:
        return 'TBD'

if __name__ == '__main__':
    is_heisei()