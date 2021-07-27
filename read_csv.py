import pandas as pd


class ReadQuestionCSV:
    def __init__(self, input_file: str):
        self.input_file = input_file

    def read_input_file(self) -> [pd.DataFrame, bool]:
        df = pd.read_csv(self.input_file, delimiter=",")
        col_count = len(df.columns)
        if col_count != 14:
            print("The column no.has changed, please check the CSV or update the code")
            return None
        return df


if __name__ == "__main__":
    r = ReadQuestionCSV("reelle-zahlen.csv")
    r.read_input_file()

