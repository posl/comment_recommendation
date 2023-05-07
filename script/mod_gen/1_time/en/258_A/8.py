def time_after_21_00(K):
    if K < 60:
        return '21:' + str(K).zfill(2)
    else:
        minutes = K % 60
        hours = (K // 60) + 21
        return str(hours) + ':' + str(minutes).zfill(2)

if __name__ == '__main__':
    time_after_21_00()