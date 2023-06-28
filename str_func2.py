def convert_to_uppercase(string):
    return string.upper()
def capitalize_words(string):
    """
    Функция принимает строку и возвращает новую строку, в которой первые буквы каждого слова заглавные.

    Аргументы:
    - string (str): Исходная строка, в которой нужно сделать заглавными первые буквы каждого слова.

    Возвращает:
    - capitalized_string (str): Новая строка с заглавными первыми буквами каждого слова.

    """

    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    capitalized_string = ' '.join(capitalized_words)
    return capitalized_string