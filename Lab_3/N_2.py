def write_array(array, file_name):
    """записывает строки из array в файл file_name"""
    file = open(file_name, "w")
    file.write('\n'.join(array))
    file.close()
    pass

