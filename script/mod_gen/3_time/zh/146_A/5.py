def get_next_sunday(s):
    days = {'SUN':0, 'MON':1, 'TUE':2, 'WED':3, 'THU':4, 'FRI':5, 'SAT':6}
    return 7 - days[s]

if __name__ == '__main__':
    get_next_sunday()