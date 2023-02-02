from typing import List

class BuildStats:
    def __init__(self, list_of_ints: List[int]):
        self.__list_of_ints = list_of_ints
    
    def less(self, value: int) -> List[int]:
        return [n for n in self.__list_of_ints if n < value]
    
    def between(self, start: int, end: int) -> List[int]:
        return [n for n in self.__list_of_ints if n > start and n < end]
    
    def greater(self, value: int) -> List[int]:
        return [n for n in self.__list_of_ints if n > value]
