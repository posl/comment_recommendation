def main():
    K = int(input())
    if K < 60:
        print('21:{:02d}'.format(K))
    elif K < 120:
        print('22:{:02d}'.format(K - 60))
    elif K < 180:
        print('23:{:02d}'.format(K - 120))
    elif K < 240:
        print('00:{:02d}'.format(K - 180))
    elif K < 300:
        print('01:{:02d}'.format(K - 240))
    elif K < 360:
        print('02:{:02d}'.format(K - 300))
    elif K < 420:
        print('03:{:02d}'.format(K - 360))
    elif K < 480:
        print('04:{:02d}'.format(K - 420))
    elif K < 540:
        print('05:{:02d}'.format(K - 480))
    elif K < 600:
        print('06:{:02d}'.format(K - 540))
    elif K < 660:
        print('07:{:02d}'.format(K - 600))
    elif K < 720:
        print('08:{:02d}'.format(K - 660))
    elif K < 780:
        print('09:{:02d}'.format(K - 720))
    elif K < 840:
        print('10:{:02d}'.format(K - 780))
    elif K < 900:
        print('11:{:02d}'.format(K - 840))
    elif K < 960:
        print('12:{:02d}'.format(K - 900))
    elif K < 1020:
        print('13:{:02d}'.format(K - 960))
    elif K < 1080:
        print('14:{:02d}'.format(K - 1020))
    elif K < 1140:
        print('15:{:02d}'.format(K - 1080))
    elif K < 1200:
        print('16:{:02d}'.format(K - 1140))
    elif K < 1260:
        print('17:{:02d}'.format(K - 1200))
    elif K < 1320:
        print('18:{:02d}'.format(K - 1260))
