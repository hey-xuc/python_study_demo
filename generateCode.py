import random

def generate_code(code_len=4):
    str = 'qwertyuiopasdflkjhzxcvbnmQWERUTYOPIASDLKFJHGZXCBVNM1234567890'
    s_len = len(str) - 1
    r_str = ''
    for i in range(code_len):
        index = random.randint(0, s_len)
        r_str += str[index]
    return r_str
    
if __name__ == '__main__':
    print(generate_code())