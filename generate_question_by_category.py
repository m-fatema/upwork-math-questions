import random
from question_by_category.category_ab import CategoryABQuestions
from question_by_category.category_d import CategoryDQuestions
from question_by_category.category_efh import CategoryEFHQuestions
from question_by_category.category_jlm import CategoryJLMQuestions
from question_by_category.category_nop import CategoryNOPQuestions
from question_by_category.category_qrst import CategoryQRSTQuestions
class GenerateQuestionByCategory:

    def __init__(self):
        self.config1 = {
            "n_roots_range": (2, 3),
            "root_range": (1, 10),
            "root_square_ratio": 0.1,
            "coefficient_range": (1, 20),
            "neg_coefficient_ration": 0.1,
        }
        pass

    def generate_category_t_question(self) -> dict:
        return CategoryQRSTQuestions().generate_category_t_question()

    def generate_category_s_question(self) -> dict:
        return CategoryQRSTQuestions().generate_category_s_question()

    def generate_category_r_question(self) -> dict:
        return CategoryQRSTQuestions().generate_category_r_question()

    def generate_category_q_question(self) -> dict:
        return CategoryQRSTQuestions().generate_category_q_question()

    def generate_category_p_question(self) -> dict:
        return CategoryNOPQuestions().generate_category_p_question()

    def generate_category_o_question(self) -> dict:
        return CategoryNOPQuestions().generate_category_o_question()

    def generate_category_n_question(self) -> dict:
        return CategoryNOPQuestions().generate_category_n_question()

    def generate_category_m_question(self):
        return CategoryJLMQuestions().generate_category_m_question()

    def generate_category_l_question(self):
        return CategoryJLMQuestions().generate_category_l_question()

    def generate_category_k_question(self):
        return {'question': 'Welcher Rechenweg sinnvoller ist, entscheidet man am besten, ' +
                            'indem man sich den Wurzelbruch genau anschaut. ' +
                            'Kann man die Wurzeln in Zähler und Nenner ',
                'correct': 'Produkt',
                'wrong_1': 'Quotienten'}

    def generate_category_j_question(self):
        return CategoryJLMQuestions().generate_category_j_question()

    def generate_category_i_question(self):
        return self.generate_category_a_question()

    def generate_category_h_question(self):
        roots, _ = self._generate_roots()
        res = CategoryEFHQuestions().generate_category_h_question(roots)
        return res

    def generate_category_f_question(self):
        roots, eq_var = self._generate_roots()
        res = CategoryEFHQuestions().generate_category_e_question(roots, eq_var)
        return res

    def generate_category_e_question(self):
        roots, eq_var = self._generate_roots()
        res = CategoryEFHQuestions().generate_category_e_question(roots, eq_var)
        return res

    def generate_category_d_question(self):
        n = self.randint(self.config1["n_roots_range"])
        equation_by_roots = list()
        answer_type = False if random.randint(0, 1) == 0 else True
        if answer_type:
            for i in range(n):
                eq_var, coeffs, root = self.get_variables_for_equation(complete_root=True)
                d = {'eq_var': eq_var,
                     'coeffs': coeffs,
                     'root': root}
                equation_by_roots.append(d)
        res = CategoryDQuestions().generate_category_d_questions(equation_by_roots)
        return res

    def generate_category_c_question(self):
        var, ans, wrong = self.form_solve_category_c_equation(category='BT')
        res = {'question':  var, 'correct:': ans, 'wrong_1': wrong}
        return res

    def generate_category_b_question(self):
        res = list()
        r = self.generate_category_a_question(category='BT')
        r['question'] = r['question'].replace("___", "? | " + r['correct'])
        res.append(r['question'])
        for i in range(3):
            r = self.generate_category_a_question(category='BF')
            r['question'] = r['question'].replace("___", " ? | " + r['correct'])
            res.append(r['question'])
        random.shuffle(res)
        res = {"question": "; ".join(res)}
        return res

    def generate_category_a_question(self, category='A'):
        eq_var, coeffs, root = self.get_variables_for_equation()
        return CategoryABQuestions().generate_question(eq_var, coeffs, root,
                                                                 category=category)

    def get_variables_for_equation(self, complete_root=False) -> [list, list, int]:
        root = self.randint(self.config1["root_range"])
        if random.random() < self.config1["root_square_ratio"] or complete_root:
            root **= 2
        coeffs = self._generate_coeffs()
        eq_var = [f'{coeffs[i]} sqrt({root})' for i in range(len(coeffs))]
        return eq_var, coeffs, root

    def _generate_coeffs(self) -> list:
        coeffs = [
            (-1 if random.random() < self.config1["neg_coefficient_ration"] else 1)
            * self.randint(self.config1["coefficient_range"])
            for _ in range(self.randint(self.config1["n_roots_range"]))
        ]
        return coeffs

    def _generate_roots(self) -> list:
        roots = [self.randint(self.config1["root_range"])
                 for _ in range(self.randint(self.config1["n_roots_range"]))]
        eq_var = [f'sqrt({root})' for root in roots]
        return roots, eq_var

    def randint(self, ranges: [int, int]) -> int:
        random_no = random.randint(ranges[0], ranges[1])
        return random_no



    ## Category C questions
    def get_var_ans_for_category_c(self, res: dict) -> [str, str]:
        var = (res['question'].split(' = ')[0].split(" + "))
        final_res = res['question'].split(' = ')[1].replace("*", "").replace(" ", "").replace("___", "")
        ans = res['correct'] + final_res
        return var, ans

    def form_solve_category_c_equation(self, category: str):
        var = list()
        ans = list()
        constant_list = list()
        coeff_list = list()
        wrong = list()
        for i in range(2):
            r = self.generate_category_a_question(category='BT')
            v, a = self.get_var_ans_for_category_c(r)
            var.extend(v)
            if 'sqrt(' not in a:
                constant_list.append(int(a))
            else:
                ans.append(a.strip())
                coeff_list.append(int(a.split('sqrt(')[0].strip()))
            root = v[0].split('sqrt(')[1][0]
            wrong.append((sum(coeff_list), root))
        answer = ''
        random.shuffle(ans)
        answer += " + ".join(a for a in ans)
        if len(constant_list) > 0:
            if answer:
                answer += " + " + str(sum(constant_list))
            else:
                answer = sum(constant_list)
        random.shuffle(var)
        wrong_str = self.generate_wrong_value(wrong)
        ques = " + ".join(var)
        return ques, answer, wrong_str

    def generate_wrong_value(self, wrong: list) -> str:
        root = self.randint((1, len(wrong)-1))
        wrong_str = ''
        random.shuffle(wrong)
        for i in range(len(wrong)):
            w = list(wrong[i])
            if i == root:
                w[0] = w[0] * (-1)
            c = 1 if w[0] == 0 else w[0]
            wrong_str += ' + ' if c > 0 else ' '
            wrong_str += str(c) + f"sqrt({w[1]})"
        wrong_str = wrong_str.strip()
        if wrong_str.startswith('+', 0, 1):
            wrong_str = wrong_str.replace('+', '', 1)
        wrong_str = wrong_str.strip()
        wrong_str = wrong_str.replace('-', '- ')
        return wrong_str

