import random
from question_by_category.category_qrst import CategoryQRSTQuestions


class CategoryUVWQuestions:

    def __init__(self, category_qrst: CategoryQRSTQuestions):
        self.category_qrst = category_qrst
        pass

    def generate_category_w_question(self) -> dict:
        question = ''
        no = random.randint(-100, 100)
        q_type = random.randint(1, 5)
        res = {}
        if q_type == 1:
            question = f'Liegt {no} im Zahlenbereich von ℕ?'
            if no > 0:
                correct, wrong_1 = self._get_correct_wrong_val('correct', 'wrong')
            else:
                correct, wrong_1 = self._get_correct_wrong_val('wrong', 'correct')
        elif q_type == 2:
            n_typ = random.choice(['ℕ', 'ℤ', 'ℚ'])
            question = f'Liegt sqrt({no}) im Zahlenbereich von {n_typ}?'
            if no > 0 and (no ** 0.5) % 1 == 0:
                correct, wrong_1 = self._get_correct_wrong_val('correct', 'wrong')
            else:
                correct, wrong_1 = self._get_correct_wrong_val('wrong', 'correct')
        elif q_type == 3:
            n_typ = random.choice(['ℚ', 'ℤ', 'ℝ'])
            question = f'Liegt {no} im Zahlenbereich von {n_typ}?'
            correct, wrong_1 = self._get_correct_wrong_val('correct', 'wrong')
        elif q_type == 4:
            question = f'Liegt sqrt({no}) im Zahlenbereich von ℝ?'
            no = no * (-1) if no < 0 else no
            if (no ** 0.5) % 1 == 0:
                no = no + 1
            correct, wrong_1 = self._get_correct_wrong_val('correct', 'wrong')
        else:
            ch = random.choice([True, False])
            if ch:
                question = f'Liegt {no} im Zahlenbereich von ℝ/ℚ?'
                correct, wrong_1 = self._get_correct_wrong_val('wrong', 'correct')
            else:
                question = f'Liegt sqrt({no}) im Zahlenbereich von ℝ/ℚ?'
                no = no * (-1) if no < 0 else no
                if (no ** 0.5) % 1 == 0:
                    correct, wrong_1 = self._get_correct_wrong_val('wrong', 'correct')
                else:
                    correct, wrong_1 = self._get_correct_wrong_val('correct', 'wrong')
            hint = 'Der Ausdruck ℝ/ℚ bedeutet: alle reellen Zahlen <i>ohne</i> die rationalen Zahlen, ' \
                   'also alle <b>irrationalen</b> Zahlen.'
            res.update({'hint': hint})
        res.update({'question': question, 'correct': correct, 'wrong_1': wrong_1})
        return res

    def _get_correct_wrong_val(self, crrct_ans: str, wrong: str):
        correct = crrct_ans
        wrong_1 = wrong
        return correct, wrong_1

    def generate_category_v_question(self) -> dict:
        question = list()
        n1 = random.randint(1, 10000)
        n2 = random.randint(1, 10000)
        question.append(f'{n1}')
        question.append(f'{n2}')
        z1 = random.randint(-10000, -1)
        z2 = random.randint(-10000, -1)
        question.append(f'{z1}')
        question.append(f'{z2}')
        q1 = round(random.uniform(10, 100), 2)
        n, d = self._get_rationa_fraction()
        q2 = f'{n}/{d}'
        q3 = self._get_rational_bar_no()
        question.append(f'{q1}')
        question.append(f'{q2}')
        question.append(f'{q3}')
        random.shuffle(question)
        res = {'question': "~".join(question),
               'correct': f'ℕ|{n1}~{n2},ℤ|{z1}~{z2},ℚ|{q1}~{q2}~{q3}'}
        return res

    def generate_category_u_question(self) -> dict:
        rational_list = self._generate_rational_values()
        irrational_list = self._generate_irrational_values()
        question = list()
        question.extend(rational_list)
        question.extend(irrational_list)
        random.shuffle(question)
        res = {'question': "~".join(question),
               'correct': f"Rational|{'~'.join(rational_list)},Irrational|{'~'.join(irrational_list)}"}
        return res

    def _generate_irrational_values(self) -> list:
        irrational_list = list()
        no = round(random.uniform(10, 100), 4)
        irrational_list.append(f'{no}...')
        pi = random.choice(['π', '-π'])
        irrational_list.append(pi)
        f1 = self._genetate_irrational_fraction()
        f2 = self._genetate_irrational_fraction()
        irrational_list.append(f'{f1[0]}/{f1[1]}')
        irrational_list.append(f'{f2[1]}/{f2[0]}')
        random.shuffle(irrational_list)
        return irrational_list

    def _genetate_irrational_fraction(self) -> list:
        n1 = random.randint(1, 100)
        while (n1 ** 0.5) % 1 == 0:
            n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        while (n2 ** 0.5) % 1 == 0:
            n2 = random.randint(1, 100)
        mul = random.choice([1, 10, 100])
        n1 = n1 * mul
        fraction = list()
        fraction.append(f'sqrt({n1})')
        fraction.append(n2)
        return fraction

    def _generate_rational_values(self) -> list:
        rational_list = list()
        _, sqr = self.category_qrst.generate_sqr_root()
        sqr = sqr/100
        rational_list.append(f'sqrt({sqr})')
        no = random.randint(-100, 100)
        rational_list.append(f'{no}')
        n, d = self._get_rationa_fraction()
        rational_list.append(f'{n}/{d}')
        bar_no = self._get_rational_bar_no()
        rational_list.append(bar_no)
        random.shuffle(rational_list)
        return rational_list

    def _get_rationa_fraction(self) -> [int, int]:
        n = random.randint(1, 100)
        d = random.randint(1, 100)
        while n > d:
            d = random.randint(1, 100)
        return n, d

    def _get_rational_bar_no(self) -> str:
        c = random.randint(1, 99)
        dec = random.randint(2, 99)
        no = f'{c}.bar({dec})'
        return no


