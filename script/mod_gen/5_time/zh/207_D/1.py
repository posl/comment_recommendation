def get_angle(a,b):
    if a==0:
        if b>0:
            return 90
        elif b<0:
            return 270
        else:
            return 0
    else:
        if a>0:
            if b>0:
                return math.degrees(math.atan(b/a))
            elif b<0:
                return 360+math.degrees(math.atan(b/a))
            else:
                return 0
        else:
            return 180+math.degrees(math.atan(b/a))

if __name__ == '__main__':
    get_angle()