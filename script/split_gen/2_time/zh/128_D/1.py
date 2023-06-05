def getSwitchState(switch_status, switch_num, bulb_num):
    if switch_num == 1:
        return [switch_status]
    else:
        switch_state = []
        for i in range(switch_num):
            if i == 0:
                switch_state.append([switch_status[i]])
            else:
                switch_state[0].append(switch_status[i])
        return switch_state
