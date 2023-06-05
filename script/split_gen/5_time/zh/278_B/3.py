def get_input():
    """获取用户输入"""
    user_input = input("请输入时间(HH:MM):")
    time = user_input.split(':')
    return time
