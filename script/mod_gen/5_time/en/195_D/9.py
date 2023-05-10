def max_value(baggage, boxes):
    #print(baggage, boxes)
    if len(baggage) == 0 or len(boxes) == 0:
        return 0
    if baggage[0][0] <= boxes[0][0]:
        return max(baggage[0][1] + max_value(baggage[1:], boxes[1:]), max_value(baggage[1:], boxes))
    else:
        return max_value(baggage[1:], boxes)

if __name__ == '__main__':
    max_value()