from buildstats import BuildStats

class DataCapture:
    
    def __init__(self):
        self.__data = []
    
    def add(self, value: int):
        self.__data.append(value)
    
    def build_stats(self) -> BuildStats:
        self.__data.sort()
        return BuildStats(self.__data)
