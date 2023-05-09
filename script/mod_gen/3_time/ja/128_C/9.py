def get_switch_state( switch_state, switch_count, switch_list, bulb_list, bulb_state, bulb_count, bulb_index ):
    if bulb_index == bulb_count:
        bulb_state_list = [ 0 for i in range( bulb_count ) ]
        for i in range( bulb_count ):
            for j in bulb_list[i]:
                bulb_state_list[i] += switch_state[j-1]
            bulb_state_list[i] %= 2
        if bulb_state_list == bulb_state:
            return 1
        else:
            return 0
    else:
        switch_state[ switch_list[bulb_index][switch_count[bulb_index]] - 1 ] = 0
        result = get_switch_state( switch_state, switch_count, switch_list, bulb_list, bulb_state, bulb_count, bulb_index + 1 )
        switch_state[ switch_list[bulb_index][switch_count[bulb_index]] - 1 ] = 1
        result += get_switch_state( switch_state, switch_count, switch_list, bulb_list, bulb_state, bulb_count, bulb_index + 1 )
        return result

if __name__ == '__main__':
    get_switch_state()