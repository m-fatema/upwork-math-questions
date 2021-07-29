import random
import numpy


class CategoryEFGHQuestions:
    def __init__(self):
        pass

    def generate_category_e_question(self, roots: list, eq_var: list) -> dict:
        prod = numpy.prod(roots)
        question = "*".join(eq_var)
        a2 = list()
        for i in range(len(roots)):
            a2.append("___")
        a2_str = " * ".join(a2)
        question += f" = sqrt({a2_str})"
        question += f" = sqrt(___)"
        roots.append(prod)
        if(prod ** 0.5) % 1 == 0:
            roots.append(int(prod ** 0.5))
            question += f" = ___"

        correct = [str(r) for r in roots]
        res = {'question': question,
               'correct': ";".join(correct)}
        return res

    def generate_category_f_question(self, roots: list, eq_var: list) -> dict:
        prod = numpy.prod(roots)
        question = "*".join(eq_var)
        question += f" = sqrt({prod})"
        if(prod ** 0.5) % 1 == 0:
            correct = 'Ja'
            wrong_1 = 'Nein'
        else:
            correct = 'Nein'
            wrong_1 = 'Ja'
        res = {'question': question,
               'correct': correct,
               'wrong_1': wrong_1}
        return res

    def generate_category_g_question(self) -> dict:
        roots = list()
        sqrs = list()
        for _ in range(2):
            r = random.randint(1, 15)
            sqr = r ** 2
            roots.append(str(r))
            sqrs.append(f'{sqr}')
        correct = f'{";".join(sqrs)};{";".join(roots)}'
        question = f'sqrt({"/".join(sqrs)})'
        question += f' = sqrt(___)/sqrt(___) = ___/___'
        res = {'question': question,
               'correct': correct}
        print(f'GGGG res: {res}')
        return res

    def generate_category_h_question(self, roots: list) -> dict:

        index = random.randint(0, len(roots))
        first_val = ''
        other_val = list()
        a2 = list()
        a3 = list()
        for i in range(len(roots)):
            r = roots[i]
            if i == index:
                if (r ** 0.5) % 1 != 0:
                    r **= 2
                    roots[i] = r
                first_val = str(int(r ** 0.5))
            else:
                other_val.append(f'sqrt({r})')
            a2.append('sqrt(___)')
            a3.append('___')
        prod = numpy.prod(roots)
        question = first_val + "*" + "*".join(other_val)
        a2_str = " * ".join(a2)
        a3_str = f"sqrt({' * '.join(a3)})"
        question += f" = {a2_str}"
        question += f" = {a3_str}"
        question += f" = sqrt(___)"
        roots.append(prod)
        if(prod ** 0.5) % 1 == 0:
            roots.append(int(prod ** 0.5))
            question += f" = ___"

        correct = [str(r) for r in roots]
        res = {'question': question,
               'correct': ";".join(correct)}
        return res