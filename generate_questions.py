from read_csv import ReadQuestionCSV
from generate_question_by_category import GenerateQuestionByCategory
from config import CSV_HEADERS, CSV_HEADERS_FROM_INPUT
import pandas as pd


class GenerateDynamicQuestions:

    def __init__(self, no_of_questions: int, input_file: str, output_file: str):
        self.input_df = ReadQuestionCSV(input_file).read_input_file()
        self.output_file = output_file
        self.no_of_questions = no_of_questions
        self.question_no_set = set()
        self.ques_by_category = GenerateQuestionByCategory()
        self.csv_in_headers = CSV_HEADERS_FROM_INPUT

    def generate_questions(self):
        if self.input_df is None:
            return
        output = list()
        output_no_res = set()
        category_list = self._get_unique_categories()
        for category in category_list:
            row = self.input_df.loc[self.input_df['category'] == category].iloc[0]
            func = self.get_function_name(category.lower())
            for i in range(self.no_of_questions):
                res = func()
                if res:
                    res.update({'category': category})
                    for header in self.csv_in_headers:
                        if header not in res:
                            res.update({header: row[header]})
                    output.append(res)
                else:
                    output_no_res.add(category)
        sequenced_out_df = self._re_order_datafrema_columns(pd.DataFrame(output))
        sequenced_out_df.to_csv(self.output_file, index=False, sep=',')
        sequenced_out_df.to_excel('output.xlsx')
        print(f'Categories Not found: {output_no_res}')

    def _get_unique_categories(self) -> list():
        category_list = list(set(self.input_df['category'].to_list()))
        category_list.sort()
        # category_list.pop('X')
        return category_list

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
    no_of_questions = 25
    GenerateDynamicQuestions(no_of_questions,
                             "reelle-zahlen-2.csv",
                             "output.csv").generate_questions()
