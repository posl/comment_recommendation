def get_lights_on_count(switches, bulbs, switch_bulbs, p):
    result = 0
    for i in range(2**switches):
        switch_state = []
        for j in range(switches):
            if (i >> j) & 1:
                switch_state.append(1)
            else:
                switch_state.append(0)
        #print(switch_state)
        bulbs_on = 0
        for k in range(bulbs):
            bulbs_on_temp = 0
            for l in range(switch_bulbs[k][0]):
                bulbs_on_temp += switch_state[switch_bulbs[k][l+1]-1]
            if bulbs_on_temp % 2 == p[k]:
                bulbs_on += 1
        if bulbs_on == bulbs:
            result += 1
    return result

if __name__ == '__main__':
    get_lights_on_count()