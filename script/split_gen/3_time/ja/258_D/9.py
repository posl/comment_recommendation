def calcTime(stages,stageNum):
    time = 0
    for stage in stages:
        time += stage[0] + stage[1] * (stageNum - 1)
    return time
