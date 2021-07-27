import random

class CategoryDQuestions():

    def __init__(self):
        pass

    def generate_category_d_questions(self, eq_var: list) -> dict:
        if len(eq_var) > 0:
            res = self.generate_correct_answer(eq_var)
        else:
            res = self.generate_wrong_answer()
        return res

    def generate_correct_answer(self, eq_var: list) -> dict:
        answers = list()
        ans_2 = list()
        ans_3 = list()
        equations = list()
        for val in eq_var:
            coeffs = val['coeffs']
            root = val['root']
            eq_var = val['eq_var']
            equations.extend(eq_var)

            a2 = str(sum(coeffs)) + f'sqrt({root})'
            ans_2.append(a2)

            a3 = str((sum(coeffs))) + f'*{int(root ** 0.5)}'
            ans_3.append(a3)

            ans = int((sum(coeffs)) * (root ** 0.5))
            answers.append(ans)

        random.shuffle(answers)
        random.shuffle(equations)
        final_ans = str(sum(answers))

        eq_str = " ".join([eq.replace('-', '- ') if eq.startswith('-') else '+ ' + eq for eq in equations])
        eq_str = eq_str.replace('+ ', '', 1) if eq_str.startswith('+') else eq_str

        ans_2_str = " ".join([a2.replace('-', '- ') if a2.startswith('-') else '+ ' + a2 for a2 in ans_2])
        ans_2_str = ans_2_str.replace('+ ', '', 1) if ans_2_str.startswith('+') else ans_2_str

        ans_3_str = " ".join([a3.replace('-', '- ') if a3.startswith('-') else '+ ' + a3 for a3 in ans_3])
        ans_3_str = ans_3_str.replace('+ ', '', 1) if ans_3_str.startswith('+') else ans_3_str

        ans_str = " ".join(['- ' + str(ans) if int(ans) < 0 else '+ ' + str(ans) for ans in answers])
        ans_str = ans_str.replace('+ ', '', 1) if ans_str.startswith('+') else ans_str

        question = eq_str + " = " + ans_2_str + " = " + ans_3_str + " = " + ans_str + " = " + final_ans
        return{'question': question,
               'correct': 'correct',
               'wrong_1': 'wrong'}

    def generate_wrong_answer(self) -> dict:
        flag = True
        root = 101
        while flag:
            root = random.randint(11, 100)
            if (root ** 0.5) % 1 != 0:
                flag = False
        digits = self.digits_in_parts(root)
        question = f'sqrt({root}) = sqrt('
        end_digits = list()
        start_digits = list()
        a2 = ''
        sqrt_list = list()
        for d in digits:
            if (d ** 0.5) % 1 == 0:
                start_digits.append(str(d))
                sqrt_list.append(d ** 0.5)
            else:
                end_digits.append(f'sqrt({d})')
        start_str = " + ".join(start_digits)
        question += start_str + ")"
        end_str = ''
        if len(end_digits) > 0:
            end_str = " + ".join(end_digits)
            question += " + " + end_str

        a2 = [f'sqrt({d})' for d in start_digits]
        question += f" = " + " + ".join(a2)
        question += " + " + end_str if len(end_digits) > 0 else ''
        question += " = " + str(int(sum(sqrt_list)))
        question += " + " + end_str if len(end_digits) > 0 else ''
        return{'question': '',
               'correct': 'wrong',
               'wrong_1': 'correct'}

    def digits_in_parts(self, root) -> list:
        flag = True
        part_list = list()
        cnt = 0
        N = root
        while flag:
            part_num = random.randint(7, 12)
            sqr = part_num ** 2
            diff = N - sqr
            fin_ans = 0
            fin_ans += sum(part_list)
            if (fin_ans == root and N == 0) or cnt > 49:
                flag = False
                if diff > 0:
                    part_list.append(N)
            if diff > 0:
                part_list.append(sqr)
                N = diff
            diff = N
            if 0 < diff < 4:
                part_list.append(diff)
                N -= diff
            elif 36 <= diff <= 48:
                part_list.append(36)
                N -= 36
            elif 25 <= diff <= 35:
                part_list.append(25)
                N -= 25
            elif 16 <= diff <= 25:
                part_list.append(16)
                N -= 16
            elif 9 <= diff <= 15:
                part_list.append(9)
                N -= 9
            elif 4 <= diff <= 8:
                part_list.append(4)
                N -= 4
            cnt += 1
        return part_list