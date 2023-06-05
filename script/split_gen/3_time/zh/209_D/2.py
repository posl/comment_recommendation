def main():
    n, q = map(int, input().split())
    road = []
    town = []
    for i in range(n-1):
        road.append(list(map(int, input().split())))
    for i in range(q):
        town.append(list(map(int, input().split())))
    for i in range(q):
        if town[i][0] == town[i][1]:
            print("Town")
        else:
            for j in range(n-1):
                if road[j][0] == town[i][0] and road[j][1] == town[i][1]:
                    print("Town")
                    break
                elif road[j][0] == town[i][1] and road[j][1] == town[i][0]:
                    print("Town")
                    break
                elif road[j][0] == town[i][0] or road[j][1] == town[i][0]:
                    if road[j][0] == town[i][1] or road[j][1] == town[i][1]:
                        print("Road")
                        break
                elif road[j][0] == town[i][1] or road[j][1] == town[i][1]:
                    if road[j][0] == town[i][0] or road[j][1] == town[i][0]:
                        print("Road")
                        break
                else:
                    print("Road")
                    break
main()
