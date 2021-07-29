import random


class CategoryZAQuestions:

    def generate_category_za_question(self) -> dict:
        v, n1, n2, op, param = self._generate_random_data()
        question = f'Der Term lautet: sqrt({param}),'
        question += f' Ungleichung aufstellen: {param} ___ 0,'
        question += f' Nach {v} umstellen: {param} ≥ 0 | ___,'
        end = ''
        pos1 = param.split(op)[0]
        if op is '-':
            question += f' -{n1}{v} ≥ ___ | ___,'
            question += f' {v} ___ ___ '
            if v not in pos1:
                end = f'-{n2};≥|≤|=;-({n2}/{n1})'
            else:
                end = f'{n2};≥|≤|=;{n2}/{n1}'
        else:
            question += f' {n1}{v} ≥ ___ | ___,'
            question += f' {v} ≥ ___ '
            end = f'-{n2};-({n2}/{n1})'

        res = {'question': question, 'correct': f'≥|≤|=;+{v}|-{v};' + end}
        print(f'\n--------------\nCAT za: {res}')
        return res

    def _generate_random_data(self) -> [str, str, str, str, str]:
        v = random.choice(['x', 'y', 'z'])
        n1 = random.randint(1, 50)
        n2 = random.randint(1, 50)
        op = random.choice(['+', '-'])
        v1 = f'{n1}{v}'
        v2 = f'{n2}'
        var_list = list()
        var_list.append(v1)
        var_list.append(v2)
        random.shuffle(var_list)
        param = f'{var_list[0]}{op}{var_list[1]}'
        return v, n1, n2, op, param
