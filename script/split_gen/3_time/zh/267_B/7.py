def split_bowling_pins(pins):
    pins = list(pins)
    #print(pins)
    if pins[0] == '0':
        return 'No'
    else:
        for i in range(1,10):
            if pins[i] == '0':
                if i < 5:
                    if pins[i+1] == '1':
                        return 'No'
                else:
                    if pins[i-1] == '1':
                        return 'No'
        return 'Yes'
