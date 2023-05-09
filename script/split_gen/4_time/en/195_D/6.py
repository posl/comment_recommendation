def get_max_value(baggage, boxes):
    max_value = 0
    for bag in baggage:
        for box in boxes:
            if box[1] >= bag[0]:
                if box[0] > max_value:
                    max_value = box[0]
    return max_value
