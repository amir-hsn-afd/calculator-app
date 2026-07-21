OPERATOR_BUTTONS = {
    '+',
    '-',
    '×',
    '÷',
    '%',
}

class Calculator:

    # =========================
    # |      Constructor      |
    # =========================

    def __init__(self):
        
        self.expression = ''

        self.just_evaluate = False

        self.actions = {
            'C' : self.clear,
            '=' : self.evaluate,
            '⌫' : self.backspace,
            '%' : self.percent,
        }

    # =========================
    # |      Public API       |
    # =========================

    def append(self, value):
        
        self.handle_after_evaluation(value)

        last_char = self.expression[-1] if self.expression else ''
        is_last_operator = last_char in OPERATOR_BUTTONS
        is_new_operator = value in OPERATOR_BUTTONS

        if is_last_operator and is_new_operator:
            self.expression = self.expression[:-1]
            self.expression += value
            return self.expression
        
        if self.replace_leading_zero(value):
            return self.expression
        
        if self.normalize_leading_decimal(value):
            return self.expression

        if self.prevent_duplicate_decimal(value):
            return self.expression

        self.expression += value
        return self.expression


    def evaluate(self):
        
        expression = self.expression

        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')

        try:
            result = eval(expression)
        except Exception:
            return self.expression

        self.expression = str(result)

        self.just_evaluate = True

        return self.expression


    def clear(self):
        
        self.expression = ''
        return self.expression


    def backspace(self):

        if self.just_evaluate:
            return self.expression
        
        if not self.expression:
            return self.expression
        
        self.expression = self.expression[:-1]

        self.normalize_empty_expression()

        return self.expression


    def percent(self):
        
        return self.convert_last_number_to_percentage()


    def press(self, button):

        if button in self.actions:
            return self.actions[button]()

        return self.append(button)

    # =========================
    # |        Helpers        |
    # =========================
    
    def get_last_number(self):

        number = ''

        for char in reversed(self.expression):

            if char in OPERATOR_BUTTONS:
                break

            number += char

        return number[::-1]
    

    def replace_last_number(self, new_value):
        
        last_number = self.get_last_number()

        if not last_number:
            return self.expression

        self.expression = self.expression[:-len(last_number)]

        self.expression += new_value

        return self.expression


    def convert_last_number_to_percentage(self):
        
        last_number = self.get_last_number()

        if not last_number:
            return self.expression
        
        try:
            percentage = float(last_number) / 100
        except ValueError:
            return self.expression

        self.replace_last_number(str(percentage))

        return self.expression


    def normalize_empty_expression(self):

        if not self.expression:
            self.expression = '0'


    def replace_leading_zero(self, value):

        last_number = self.get_last_number()

        if last_number != '0':
            return False
        
        if value == '0':
            return True
        
        if value == '.':
            return False
        
        if value.isdigit():

            self.expression = self.expression[:-1]
            self.expression += value

            return True

        return False
    
    # =========================
    # |         Rules         |
    # =========================

    def prevent_duplicate_decimal(self, value):

        if value != '.':
            return False
        
        last_number = self.get_last_number()

        if '.' in last_number:
            return True
        
        return False


    def normalize_leading_decimal(self, value):

        if value != '.':
            return False
        
        last_number = self.get_last_number()

        if last_number != '':
            return False
        
        self.expression += '0.'

        return True
    

    def handle_after_evaluation(self, value):

        if not self.just_evaluate:
            return False
        
        if value in OPERATOR_BUTTONS:
            self.just_evaluate = False
            return False
        
        self.expression = ''

        self.just_evaluate = False

        return False
    

