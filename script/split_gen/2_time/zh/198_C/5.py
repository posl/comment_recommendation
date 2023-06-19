def move(R, X, Y):
    step = 0
    while X != 0 or Y != 0:
        if X > 0 and Y > 0:
            if X > Y:
                X -= R
            else:
                Y -= R
        elif X > 0 and Y < 0:
            if X > abs(Y):
                X -= R
            else:
                Y += R
        elif X < 0 and Y > 0:
            if abs(X) > Y:
                X += R
            else:
                Y -= R
        elif X < 0 and Y < 0:
            if abs(X) > abs(Y):
                X += R
            else:
                Y += R
        elif X == 0 and Y > 0:
            Y -= R
        elif X == 0 and Y < 0:
            Y += R
        elif X > 0 and Y == 0:
            X -= R
        elif X < 0 and Y == 0:
            X += R
        else:
            break
        step += 1
    return step
