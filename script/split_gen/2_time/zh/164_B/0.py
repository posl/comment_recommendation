def sheep_wolf(sheep,wolf):
    if wolf >= sheep:
        print("不安全")
    else:
        print("安全")
sheep,wolf = map(int,input().split())
sheep_wolf(sheep,wolf)
