def canHit(V, T, S, D):
    if V*T <= D <= V*S:
        return False
    else:
        return True
