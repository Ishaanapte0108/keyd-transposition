import pandas as pd
import math


class keyedtransposition:
    def __init__(self, string, key, action) -> None:
        self.string = string
        self.key = key
        self.usedIndexes = []
        self.transformedText = []
        self.col = ['plainText', 'cipherText'] if action == 0 else [
            'cipherText', 'plainText']
        self.transform()

    def calc(self, num):
        indexes = self.df['keys'][self.df['keys'].eq(num)].index[:]
        index = next(filter(lambda x: x not in self.usedIndexes, indexes), 0)
        self.usedIndexes.append(index)
        self.transformedText.append(self.df.at[index, self.col[0]])

    def transform(self):
        self.df = pd.DataFrame({self.col[0]: [char for char in self.string]})
        rows = len(self.df)
        repeatedKey = (self.key * math.ceil(rows/len(self.key)))[:rows]
        self.df['keys'] = list(map(str, repeatedKey))
        self.df['position'] = self.df['keys'].sort_values().values
        self.df['position'].map(self.calc)
        self.df[self.col[1]] = self.transformedText
        ttx = '' .join(self.transformedText)
        print(self.df)
        print("Value: ", ttx)
