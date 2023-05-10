def check_light(light, on_off):
    cnt = 0
    for i in light[1:]:
        if on_off[i-1] == 1:
            cnt += 1
    if cnt % 2 == light[0]:
        return True
    else:
        return False
