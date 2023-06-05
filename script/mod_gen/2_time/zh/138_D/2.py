def get_max_value_of_last_ingredient(ingredient_list):
    # 从大到小排序
    ingredient_list.sort(reverse=True)
    # 从最大的两个开始计算
    while len(ingredient_list) > 1:
        # 取出最大的两个值
        max_value1 = ingredient_list.pop(0)
        max_value2 = ingredient_list.pop(0)
        # 计算并添加到列表
        ingredient_list.append((max_value1 + max_value2) / 2)
        # 从大到小排序
        ingredient_list.sort(reverse=True)
    # 取出最后一个值
    max_value = ingredient_list.pop()
    return max_value

if __name__ == '__main__':
    get_max_value_of_last_ingredient()