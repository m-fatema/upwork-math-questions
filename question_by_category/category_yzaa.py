import random
from sympy import expand, symbols


class CategoryYZAAQuestions:

    def generate_category_aa_question(self) -> dict:
        res={}
        return res

    def generate_category_z_question(self) -> dict:
        question = list()
        answer = list()
        correct = ''

        _, _, _, param = self._generate_random_data()
        ques, ans = self._generate_question_z1(param)
        correct += f'{ques}=?|{ans},'
        question.append(ques)
        answer.append(ans)

        v1, v2, op, _ = self._generate_random_data()
        ques, ans = self._generate_question_z2(v1, v2, op)
        correct += f'{ques}=?|{ans},'
        question.append(ques)
        answer.append(ans)

        _, _, _, param = self._generate_random_data()
        ques, ans = self._generate_question_z3(param)
        correct += f'{ques}=?|{ans}'
        question.append(ques)
        answer.append(ans)

        random.shuffle(question)
        random.shuffle(answer)
        q = "~".join(question) + "|" + "~".join(answer)
        res = {'question': q, 'correct': correct}
        print(f'\nres:{res}')
        return res

    def _generate_random_data(self) -> [str, str, str, str]:
        v = random.choice(['x', 'y', 'z'])
        n1 = random.randint(1, 50)
        n2 = random.randint(1, 50)
        op = random.choice(['+', '-', ''])
        v1 = f'{n1}{v}'
        v2 = f'{n2}'
        if op:
            param = f'{v1}{op}{v2}'
        else:
            param = f'{v1}'
        return v1, v2, op, param

    def _generate_question_z1(self, param) -> [str, str]:
        q = f'sqrt(({param})^2)'
        a = f'{param}'
        return q, a

    def _generate_question_z2(self, v1, v2, op) -> [str, str]:
        if not op:
            op = random.choice(['+', '-'])
        ans_v1 = f'sqrt({v1})'
        ans_v2 = f'sqrt({v2})'
        if bool(random.getrandbits(1)):
            ans_v1 = f'{v1}'
            v1 = f'{v1}^2'
        if bool(random.getrandbits(1)):
            ans_v2 = f'{v2}'
            v2 = f'{v2}^2'
        q = f'sqrt({v1}){op}sqrt({v2})'
        a = f'{ans_v1}{op}{ans_v2}'
        return q, a

    def _generate_question_z3(self, param) -> [str, str]:
        root = random.randint(2, 20)
        sqr = root ** 2
        q = f'sqrt(({param})^{sqr})'
        a = f'({param})^{root}'
        return q, a

    def generate_category_y_question(self) -> dict:
        ch = random.randint(1, 3)
        no = random.randint(1, 9)
        v1 = random.choice(['x', 'y', 'z', 'r', ''])
        v2 = random.choice(['a', 'b', 'c', 's'])
        is_sqrt = random.choice([True, False])
        var1 = f'sqrt({no}{v1})' if is_sqrt else f'{no}{v1}'
        is_sqrt = random.choice([True, False])
        var2 = f'sqrt({v2})' if is_sqrt else f'{v2}'
        a = {'var': var1, 'v': v1, "c": no}
        b = {'var': var2, 'v': v2}
        var_list = list()
        var_list.append(a)
        var_list.append(b)
        random.shuffle(var_list)
        if ch == 1:
            question = self._solve_binomial_formula_1(var_list[0], var_list[1], "+")
            correct = 'erste'
            wrong = list(['zweite', 'dritte'])
        elif ch == 2:
            question = self._solve_binomial_formula_1(var_list[0], var_list[1], "-")
            correct = 'zweite'
            wrong = list(['dritte', 'erste'])
        else:
            question = self._solve_binomial_formula_3(var_list[0], var_list[1])
            correct = 'dritte'
            wrong = list(['zweite', 'erste'])
        random.shuffle(wrong)
        res = {'question': question, 'correct': correct, 'wrong_1': wrong[0], 'wrong_2': wrong[1]}
        return res

    def _solve_binomial_formula_3(self, a_dict: dict, b_dict: dict) -> str:
        a = a_dict.get("var")
        b = b_dict.get("var")
        q = f'({a}+{b})({a}-{b})'
        q += f' = ({a})^2 - ({b})^2'
        if 'sqrt' in q:
            if 'sqrt' in a:
                ans_a = f'{a_dict.get("c", "")}{a_dict.get("v", "")}'
            else:
                ans_a = f'({a})^2'

            if 'sqrt' in b:
                ans_b = f'{b_dict.get("c", "")}{b_dict.get("v", "")}'
            else:
                ans_b = f'({a})^2'
            q += f' = {ans_a} - {ans_b}'
        return q

    def _solve_binomial_formula_1(self, a_dict: dict, b_dict: dict, op: str) -> str:
        a = a_dict.get("var")
        b = b_dict.get("var")
        if 'c' in a_dict:
            no = a_dict.get('c')
        else:
            no = b_dict.get('c')
        variables = f'{a} {b}'
        variables = variables.strip()
        formula_a, formula_b = symbols(variables)
        if op == '+':
            expr = formula_a + formula_b
        else:
            expr = formula_a - formula_b
        q = f'({a}{op}{b})^2'
        q += f'= ({a})^2 {op} 2*({a})*({b}) + ({b})^2'
        ans_str = str(expand(expr**2))
        ans_str = ans_str.replace("**", "^")
        if op == '+':
            ans = ans_str.split(" + ")
        else:
            a1 = ans_str.split(" + ")
            a2 = a1[0].split(" - ")
            ans = list()
            ans.extend(a2)
            ans.append(a1[1])

        if 'sqrt' in ans_str:
            if 'sqrt' in ans[0]:
                ans[0] = self._get_variable_loc(ans[0], str(formula_a), a_dict, b_dict)
            if 'sqrt' in ans[2]:
                ans[2] = self._get_variable_loc(ans[2], str(formula_a), a_dict, b_dict)
        else:
            ans[1] = ans[1].replace('*', '').replace('2', '').replace(f'{no}', '')
            ans[1] = f'{2*no}{ans[1]}'

        if op == '+':
            ans_str = " + ".join(ans)
        else:
            ans_str = f'{ans[0]} - {ans[1]} + {ans[2]}'

        q += f' = {ans_str}'
        return q

    def _get_variable_loc(self, ans: str, pos1: str, a_dict: dict, b_dict: dict) -> str:
        if pos1 in ans:
            ans = self._get_sqrt_val(a_dict)
        else:
            ans = self._get_sqrt_val(b_dict)
        return ans

    def _get_sqrt_val(self, val):
        v = val.get('v', '')
        c = val.get('c', '')
        c = '' if c == 1 else c
        value = f'{c}{v}'
        return value

    def _reformat_sqrt_values(self, val) -> str:
        formula_val = val
        if 'sqrt' in val:
            formula_val = val.replace('sqrt', '')
            formula_val += f'** 0.5'
        return formula_val
