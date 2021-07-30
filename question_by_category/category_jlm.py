import random


class CategoryJLMQuestions:
    def __init__(self):
        pass

    def generate_category_j_question(self) -> dict:
        val2 = random.randint(3, 15)
        val1 = val2 * random.randint(2, 10)
        question = f'sqrt({val1}) / sqrt({val2})'
        question += f'= sqrt(___/___)'
        question += f'= sqrt(__)'
        ans = int(val1/val2)
        correct = str(val1) + ";" + str(val2) + ";" + str(ans)
        if(ans ** 0.5) % 1 == 0:
            question += f'= __'
            fin_ans = int(ans ** 0.5)
            correct += ";" + str(fin_ans)

        res = {'question': question,
               'correct': correct}
        return res

    def generate_category_l_question(self) -> dict:
        ch = bool(random.getrandbits(1))
        if ch:
            res = self._generate_question_l1()
        else:
            res = self._generate_question_l2()
        return res

    def _generate_question_l1(self) -> dict:
        r = random.randint(1, 15)
        r2 = r * random.randint(2, 15)
        # quotient = int(r2 / r)
        wrong_1 = f'sqrt({r2})/ sqrt({r})'
        correct = f'sqrt({r2}/{r})'  # = sqrt({quotient})'
        # if (quotient ** 0.5) % 1 == 0:
        #     correct += f' = {int(quotient  ** 0.5)}'
        res = {'question': '',
               'correct': correct,
               'wrong_1': wrong_1}
        return res

    def _generate_question_l2(self) -> dict:
        r1 = random.randint(2, 15)
        sqr1 = r1 ** 2
        r2 = random.randint(1, 15)
        sqr2 = r2 ** 2
        correct = f'sqrt({sqr1})/sqrt({sqr2})'  #' = {r1}/{r2}'
        wrong_1 = f'sqrt({sqr1}/{sqr2})'
        # if sqr1 % sqr2 == 0:
        #     correct += f' = {int(sqr1/sqr2)}'
        res = {'question': '',
               'correct': correct,
               'wrong_1': wrong_1}
        return res

    def generate_category_m_question(self) -> dict:
        ans = list()
        for _ in range(2):
            r = random.randint(1, 15)
            ans.append(r)
        n = ans[0]
        d = ans[1]
        question = f'sqrt({n}/{d})'
        if (d ** 0.5) % 1 == 0:
            question += f' = sqrt(___)/sqrt(___)'
            d2 = int(d ** 0.5)
            if (n ** 0.5) % 1 == 0:
                n = int(n ** 0.5)
                question += f' = ___/___'
                ans.append(n)
                ans.append(d2)
            else:
                question += f' = sqrt({n})/{d2}'
                question += f' = ___/___ sqrt(___)'
                ans.append(1)
                ans.append(d2)
                ans.append(n)
        else:
            random_type_2_3 = bool(random.getrandbits(1))
            if random_type_2_3:
                question, ans = self.generate_m2_eq(n, d, question)
            else:
                question, ans = self.generate_m3_eq(n, d)

        res = {'question': question,
               'correct': ";".join([str(a) for a in ans])}
        return res

    def generate_m2_eq(self, n: int, d: int, question: str) -> [str, list]:
        ans = list()
        ans.append(d)
        ans.append(d)
        question += f' = sqrt(({n}*___)/({d}*___))'

        n = n * d
        question += f' = sqrt({n})/{d}'

        ans.append(1)
        ans.append(d)
        ans.append(n)
        question += f' = ___/___ sqrt(___)'
        return question, ans

    def generate_m3_eq(self, n: int, d: int) -> [str, list]:
        question = f'{n}/sqrt({d})'
        ans = list()
        ans.append(f'sqrt({d})')
        ans.append(f'sqrt({d})')
        question += f' = ({n}*___)/sqrt({d})*___'
        question += f' = ({n}*sqrt({d}))/{d}'
        ans.append(n)
        ans.append(d)
        ans.append(d)
        question += f' = ___/___ sqrt(___)'
        return question, ans
