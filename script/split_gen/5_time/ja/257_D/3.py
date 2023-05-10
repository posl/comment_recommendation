def check_jump(start,goal):
    return P[start]*S >= abs(X[start]-X[goal]) + abs(Y[start]-Y[goal])
