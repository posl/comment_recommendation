def get_light_num(num, switch, light):
    switch_num = len(switch)
    switch_status = [0] * switch_num
    light_status = [0] * light
    for i in range(num):
        for j in range(switch_num):
            if (i + 1) in switch[j]:
                switch_status[j] += 1
    for i in range(switch_num):
        switch_status[i] = switch_status[i] % 2
    for i in range(switch_num):
        for j in range(light):
            if (j + 1) in switch[i]:
                light_status[j] += switch_status[i]
    for i in range(light):
        light_status[i] = light_status[i] % 2
    if light_status.count(1) == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    get_light_num()