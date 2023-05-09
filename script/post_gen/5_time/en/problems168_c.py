Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    import math
    a, b, h, m = map(int, input().split())
    h_angle = (h * 60 + m) * 0.5
    m_angle = m * 6
    angle = abs(h_angle - m_angle)
    angle = min(angle, 360 - angle)
    angle = math.radians(angle)
    ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle))
    print(ans)

=======
Suggestion 2

def main():
    import math
    a, b, h, m = map(int, input().split())
    h_angle = (h * 60 + m) / 720 * 360
    m_angle = m / 60 * 360
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle)))
    print(ans)

=======
Suggestion 3

def main():
    import math
    A, B, H, M = map(int, input().split())
    angle = abs(30*H - 5.5*M)
    if angle > 180:
        angle = 360 - angle
    ans = (A**2 + B**2 - 2*A*B*math.cos(math.radians(angle)))**0.5
    print(ans)

=======
Suggestion 4

def main():
    import math
    A, B, H, M = map(int, input().split())
    a = 2 * math.pi * (H / 12 + M / 720)
    b = 2 * math.pi * (M / 60)
    c = a - b
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(c)))

=======
Suggestion 5

def main():
    import math
    a,b,h,m = map(int,input().split())
    h_angle = h*30 + m*0.5
    m_angle = m*6
    angle = abs(h_angle-m_angle)
    x = a**2 + b**2 - 2*a*b*math.cos(math.radians(angle))
    print(math.sqrt(x))

=======
Suggestion 6

def main():
    import math
    A, B, H, M = map(int, input().split())
    ans = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(30*H+M/2)))
    print(ans)

=======
Suggestion 7

def main():
    import math
    a,b,h,m = map(int,input().split())
    print(math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(30*(h+m/60)-6*m))))

=======
Suggestion 8

def main():
    # Get input here
    A, B, H, M = map(int, input().strip().split())

    # Calculate result here
    hour_angle = 0.5 * (H * 60 + M)
    minute_angle = 6 * M
    angle = abs(hour_angle - minute_angle)
    if angle > 180:
        angle = 360 - angle
    import math
    ans = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(angle)))

    # Print result here
    print(ans)

=======
Suggestion 9

def main():
    a, b, h, m = map(int, input().split())
    import math
    theta = abs((h*60+m)/720*360 - m/60*360)
    print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta))))

=======
Suggestion 10

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
