def get_sea_view_count(mountain_list):
    """
    计算可以看到海景的旅馆数量
    :param mountain_list: 山峰高度列表
    :return: 可以看到海景的旅馆数量
    """
    # 从第一个开始遍历
    sea_view_count = 1
    # 从第二个开始遍历
    for index in range(1, len(mountain_list)):
        # 从第一个开始遍历
        for pre_index in range(0, index):
            # 判断是否可以看到海景
            if mountain_list[pre_index] > mountain_list[index]:
                # 不可以看到海景，跳出循环
                break
        else:
            # 可以看到海景，计数加1
            sea_view_count += 1
    return sea_view_count

if __name__ == '__main__':
    get_sea_view_count()