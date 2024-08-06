class DataModel:
    def __init__(self, column1, column2):
        self.column1 = column1
        self.column2 = column2

    def to_tuple(self):
        return (self.column1, self.column2)
