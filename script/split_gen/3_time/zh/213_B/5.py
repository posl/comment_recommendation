def getSecondLowestScorePlayerIndex(scores):
    """获取第二低分玩家的索引"""
    # 先排序
    scores.sort(reverse=True)
    # 找到第二低分
    secondLowestScore = scores[0]
    for score in scores:
        if score < secondLowestScore:
            secondLowestScore = score
            break
    # 找到第二低分玩家的索引
    for index, score in enumerate(scores):
        if score == secondLowestScore:
            return index
