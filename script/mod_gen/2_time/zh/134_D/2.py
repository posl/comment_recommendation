def print_good_choice_set(N, arr):
    # 1. find all the balls
    # 2. find all the boxes
    # 3. find all the boxes which are multiple of the ball
    # 4. if the total number of balls in the boxes are even, then it is a good choice set
    # 5. if the total number of balls in the boxes are odd, then it is a bad choice set
    # 6. if it is a bad choice set, then return -1
    # 7. if it is a good choice set, then return the ball number in the boxes
    # 8. if there is no ball in the boxes, then return 0
    # 1. find all the balls
    balls = []
    for i in range(N):
        if arr[i] == 1:
            balls.append(i+1)
    # 2. find all the boxes
    boxes = []
    for i in range(N):
        boxes.append(i+1)
    # 3. find all the boxes which are multiple of the ball
    multiple_boxes = []
    for ball in balls:
        for box in boxes:
            if box % ball == 0:
                multiple_boxes.append(box)
    # 4. if the total number of balls in the boxes are even, then it is a good choice set
    # 5. if the total number of balls in the boxes are odd, then it is a bad choice set
    # 6. if it is a bad choice set, then return -1
    # 7. if it is a good choice set, then return the ball number in the boxes
    # 8. if there is no ball in the boxes, then return 0
    if len(multiple_boxes) == 0:
        print(0)
    elif len(multiple_boxes) % 2 == 0:
        print(len(multiple_boxes))
        for box in multiple_boxes:
            print(box)
    else:
        print(-1)

if __name__ == '__main__':
    print_good_choice_set()