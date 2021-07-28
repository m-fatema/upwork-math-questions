import random


class CategoryQRSTQuestions():
    def __init__(self):
        pass

    def generate_category_q_question(self) -> dict:
        cube_rt = random.randint(2, 10)
        cube = cube_rt ** 3
        ans = list()
        question = f'V = {cube};'
        ans.append(cube)
        question += f'a = root3(___ m^3)'
        ans.append(cube_rt)
        question += f' = ___ m'
        res = {'question': question,
               'correct': ';'.join([str(a) for a in ans])}
        return res

    def generate_category_r_question(self) -> dict:
        correct = list()
        for i in range(5):
            root, sqr = self.generate_sqr_root()
            correct.append(f'x=sqrt({sqr})|{root}')
        res = {'question': '',
               'correct': ';'.join([str(a) for a in correct])}
        return res

    def generate_category_s_question(self) -> dict:
        root, sqr = self.generate_sqr_root()
        correct = f'x=sqrt({sqr})'
        ans = f'{root}'
        res = {'question': 'Wie lautet das Ergebnis für diese Quadratwurzel?',
               'correct': correct,
               'wrong_1': ans}
        return res

    def generate_category_t_question(self) -> dict:
        root, sqr = self.generate_sqr_root()
        correct = f'sqrt({sqr})=___'
        ans = f'{root};'
        correct += f';sqrt({sqr/100})=___'
        ans += f'{root/10}'
        res = {'question': '',
               'correct': correct,
               'wrong_1': ans}
        return res

    def generate_sqr_root(self) -> [int, int]:
        root = random.randint(2, 20)
        sqr = root ** 2
        return root, sqr
