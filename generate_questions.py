from read_csv import ReadQuestionCSV
from generate_question_by_category import GenerateQuestionByCategory
import random
from config import CSV_HEADERS, CSV_HEADERS_FROM_INPUT
import pandas as pd


class GenerateDynamicQuestions:
    def __init__(self, input_file: str, output_file: str):
        self.input_df = ReadQuestionCSV(input_file).read_input_file()
        self.output_file = output_file
        self.no_of_questions = 25
        self.question_no_set = set()
        self.question_no_set.add(39)
        self.question_no_set.add(40)
        self.question_no_set.add(41)
        self.question_no_set.add(42)
        self.question_no_set.add(43)
        self.question_no_set.add(44)
        self.question_no_set.add(45)
        self.question_no_set.add(46)
        self.question_no_set.add(47)
        self.ques_by_category = GenerateQuestionByCategory()
        self.csv_in_headers = CSV_HEADERS_FROM_INPUT

    def randint(self, ranges: [int, int]) -> int:
        random_no = random.randint(ranges[0], ranges[1])
        return random_no

    def generate_question_sequence(self, max_question_count: int):
        while len(self.question_no_set) <= self.no_of_questions:
            q = self.randint((0, max_question_count))
            self.question_no_set.add(q)

    def generate_questions(self):
        if self.input_df is None:
            return
        output = list()
        max_questions = self.input_df.shape[0] - 1
        max_questions = 42
        self.generate_question_sequence(max_questions)
        for i in self.question_no_set:
            row = self.input_df.loc[i]
            category = str(row['category']).lower()
            if category is not 'nan' and category is not 'NaN' \
                    and type(category) is not float:
                func = self.get_function_name(category)
                res = func()
                if res:
                    for header in self.csv_in_headers:
                        res.update({header: row[header]})
                    output.append(res)
                # print(f'{i}-->{category}--->{res}')
        sequenced_out_df = self._re_order_datafrema_columns(pd.DataFrame(output))
        sequenced_out_df.to_csv(self.output_file, index=False, sep=',')

    def _re_order_datafrema_columns(self, out_df: pd.DataFrame) -> pd.DataFrame:
        if 'wrong_1' not in out_df:
            out_df['wrong_1'] = ""
        if 'wrong_2' not in out_df:
            out_df['wrong_2'] = ""
        if 'wrong_3' not in out_df:
            out_df['wrong_3'] = ""
        if 'correct' not in out_df:
            out_df['correct'] = ""
        out_df[""] = ""
        out_df = out_df.rename(columns={'type': 'q_type'})
        sequenced_out_df = out_df[CSV_HEADERS]
        return sequenced_out_df

    @staticmethod
    def _func_not_found():  # just in case we don't have the function
        """
        Just in case a function is not found when we are dynamically forming function name from strings
        :param category_name: category_name
        :return:
        """
        pass

    def get_function_name(self, category_name: str) -> callable:
        """
        Generate function name according to the data type
        :param category_name: type value from the schema
        :return: function which will generate the question according to type
        """
        func_name = "generate_category_" + category_name + "_question"
        func = getattr(self.ques_by_category, func_name, self._func_not_found)
        return func


if __name__ == "__main__":
    GenerateDynamicQuestions("reelle-zahlen-2.csv", "output.csv").generate_questions()
