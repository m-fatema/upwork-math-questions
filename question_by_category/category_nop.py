import random


class CategoryNOPQuestions():
    def __init__(self):
        pass

    def generate_category_p_question(self) -> dict:
        ques_list = list()
        true_roots = list()
        not_roots = list()
        for i in range(3):
            sqr = (random.randint(2, 12)) ** 2
            ques_list.append(f'sqrt({sqr})')
            true_roots.append(f'sqrt({sqr})')
        while len(ques_list) < 6:
            root = random.randint(2, 100)
            if(root ** 0.5) % 1 != 0:
                ques_list.append(f'sqrt({root})')
                not_roots.append(f'sqrt({root})')
        random.shuffle(ques_list)
        question = '|'.join(ques_list)
        correct = 'natürliche Zahl|' + "~".join(true_roots)
        correct += ';nicht abbrechende Dezimalzahl|' + "~".join(not_roots)
        res = {'question': question, 'correct': correct}
        return res

    def generate_category_o_question(self) -> dict:
        root = random.randint(2, 12)
        ch = random.choice([1, 10, 100, 10, 10, 100])
        correct = root * ch
        sqr = correct ** 2
        question = f'sqrt({sqr})'
        res = {'question': question, 'correct': correct}
        return res

    def generate_category_n_question(self) -> dict:
        val = random.randint(1, 3)
        if val == 1:
            question, correct, wrong = self._generate_category_n1_question()
        elif val == 2:
            question, correct, wrong = self._generate_category_n2_question()
        else:
            question, correct, wrong = self._generate_category_n3_question()
        random.shuffle(wrong)
        res = {'question': question, 'correct': correct, 'wrong_1': wrong[0], 'wrong_2': wrong[1]}
        return res

    def _generate_category_n1_question(self):
        root = random.randint(2, 12)
        question = f'x^2={root ** 2}'
        correct = '2'
        wrong = list()
        wrong.append('keine')
        wrong.append('2')
        return question, correct, wrong

    def _generate_category_n2_question(self):
        sub_typ = random.randint(1, 2)
        if sub_typ == 1:
            root = (-1)*random.randint(1, 100)
            question = f'x=sqrt({root})'
        else:
            root = random.randint(1, 10)
            if(root ** 0.5) % 1 != 0:
                root = root ** 2
            question = f'x^2={(-1) * root}'
        correct = 'keine'
        wrong = list()
        wrong.append('1')
        wrong.append('2')
        return question, correct, wrong

    def _generate_category_n3_question(self):
        root = random.randint(2, 15)
        if (root ** 0.5) % 1 != 0:
            root = root ** 2
        question = f'x=sqrt({root})'
        correct = '1'
        wrong = list()
        wrong.append('2')
        wrong.append('keine')
        return question, correct, wrong
