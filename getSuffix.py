def get_suffix(filename='', has_dot=False):
    """
    :filename: 文件名
    :param has_dot: 返回文件名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')   # 返回字符在字符串中的位置
    if 0 < pos < len(filename):
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
        
    