import numpy as np
romans_numbers = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 }

def convert(main_string):
    if main_string.isdigit():
        decimal_num = int(main_string)
        try:
            if decimal_num > 5000:
                return "Number is too big! Try less than 5000."
            else:
                result_array = []
                decimal_str = str(decimal_num)
                power = len(decimal_str)-1
                for item in decimal_str:
                    letter = list(romans_numbers.keys())[list(romans_numbers.values()).index(10**power)]
                    for i in range(int(item)):
                        result_array.append(letter)
                    power -= 1
                result_str = "".join(result_array)

                for ind, item in enumerate(romans_numbers.keys()):
                    sub = item * 9
                    if (result_str.find(sub) >= 0) and (ind-2) >= 0:
                        str_l = item + list(romans_numbers.keys())[ind-2]
                        result_str = result_str.replace(sub,str_l)
                    sub = item * 5
                    if (result_str.find(sub) >= 0) and (ind-1) >= 0:
                        str_l = list(romans_numbers.keys())[ind-1]
                        result_str = result_str.replace(sub,str_l)
                    sub = item * 4
                    if (result_str.find(sub) >= 0) and (ind-1) >= 0:
                        str_l = item + list(romans_numbers.keys())[ind-1]
                        result_str = result_str.replace(sub,str_l)
                return result_str
        except:
            return "Error: Wrong symbols"
            pass
    else:
        roman_num = main_string
        try:
            result_array = []
            for ind, item in enumerate(roman_num):        
                value = romans_numbers[item]
                if ind < len(roman_num)-1 and romans_numbers[roman_num[ind+1]] > value:
                    value = -value
                result_array.append(value)

            result_array = np.array(result_array)
            result_str = np.sum(result_array)

            return str(result_str)
        except:
            return "Error: Wrong letters"
            pass