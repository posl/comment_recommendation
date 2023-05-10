def get_distance_between_hands(A,B,H,M):
    #calculate angle of hour hand
    angle_of_hour_hand = (H*60+M)/720*360
    #calculate angle of minute hand
    angle_of_minute_hand = M/60*360
    #calculate angle between hands
    angle_between_hands = abs(angle_of_hour_hand-angle_of_minute_hand)
    #calculate distance between hands
    distance_between_hands = (A**2+B**2-2*A*B*math.cos(math.radians(angle_between_hands)))**0.5
    return distance_between_hands
