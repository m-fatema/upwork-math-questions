import random


class CategoryABQuestions:
    def __init__(self):
        pass

    def generate_question(self, eq_var: list, coeffs: list, root: int, category='A'):
        correct = [*list(coeffs), sum(coeffs)]
        answer = (
                " ".join(
                    f"{'' if coeffs[i] < 0 else '+ ' if i else ''}{eq_var[i]}"
                    for i in range(len(coeffs))
                )
                + " = "
        ).replace("-", "- ")
        if answer.startswith("-"):
            answer = answer[0] + answer[2:]
        answer += (
                    "( "
                    + " ".join(
                          f"___ {('-' if coeffs[i + 1] < 0 else '+') if i < len(coeffs) - 1 else ''}"
                          for i in range(len(coeffs))
                        )
                    + ")"
                  ) + f"sqrt({root}) = ___ * sqrt({root})"

        correct, answer = self.format_output_for_category_a_b(root, correct, answer, category, coeffs)
        res = {
            "question": answer,
            "correct": ";".join(str(n) for n in correct),
        }

        return res

    def format_output_for_category_a_b(self, root: int, correct: list, answer: str,
                                       category: str, coeffs: list) -> [list, str]:
        if category == 'A':
            if (root ** 0.5) % 1 == 0:
                correct = self.get_final_ans_for_sum(root, correct, sum(coeffs))
                answer += f" = ___ * ___ = ___"
        elif category == 'BT' or category == 'BF':
            if category == 'BF':
                offset = random.randint(-10, 10)
                offset = offset if offset != 0 else -1
                coeffs.append(offset)
            if (root ** 0.5) % 1 == 0:
                correct = [self.get_final_ans_for_sum(root, correct, sum(coeffs))[-1]]
                answer += " = ___"
            else:
                correct = [correct[-1]] if category == 'BT' else [sum(coeffs)]
            ans = answer.split(' = ')
            answer = ans[0] + " = " + ans[-1]
        return correct, answer

    def get_final_ans_for_sum(self, root: int, correct: list, coeffs: int) -> list:
        correct += [int(root ** 0.5)]
        correct += [coeffs * correct[-1]]
        return correct