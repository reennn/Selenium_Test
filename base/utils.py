from typing import List


class Utils:

    # метод создания строки из списка
    @staticmethod
    def join_strings(str_list: List[str]) -> str:
        return ', '.join(str_list)
