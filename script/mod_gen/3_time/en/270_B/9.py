def main():
    #Get input
    x,y,z = map(int, input().split())
    #Calculate distance to goal
    dist_goal = abs(x)
    #Calculate distance to hammer
    dist_hammer = abs(z)
    #Calculate distance to wall
    dist_wall = abs(y)
    #If hammer is before wall, then go get the hammer
    if dist_hammer < dist_wall:
        #Calculate distance to hammer and back
        dist_hammer = dist_hammer + dist_hammer
        #Calculate total distance
        dist_total = dist_hammer + dist_goal
        #Print total distance
        print(dist_total)
    #If hammer is after wall, then go to goal
    elif dist_hammer > dist_wall:
        #Calculate total distance
        dist_total = dist_goal
        #Print total distance
        print(dist_total)
    #If hammer is at wall, then go to goal
    elif dist_hammer == dist_wall:
        #Calculate total distance
        dist_total = dist_goal
        #Print total distance
        print(dist_total)
    #If hammer is at goal, then go to goal
    elif dist_hammer == dist_goal:
        #Calculate total distance
        dist_total = dist_goal
        #Print total distance
        print(dist_total)
    #If hammer is at origin, then go to goal
    elif dist_hammer == 0:
        #Calculate total distance
        dist_total = dist_goal
        #Print total distance
        print(dist_total)
    #If goal is at origin, then go to hammer
    elif dist_goal == 0:
        #Calculate total distance
        dist_total = dist_hammer
        #Print total distance
        print(dist_total)
    #If hammer and goal are at the same location, then go to hammer
    elif dist_goal == dist_hammer:
        #Calculate total distance
        dist_total = dist_hammer
        #Print total distance
        print(dist_total)
    #If hammer and goal are at the same location, then go to hammer
    elif dist_goal == dist_hammer:
        #Calculate total distance
        dist_total = dist_hammer
        #Print total distance
        print(dist_total)
    #If hammer is at wall, then go to goal
    elif dist_hammer == dist_wall:
        #Calculate total distance
        dist_total = dist

if __name__ == '__main__':
    main()