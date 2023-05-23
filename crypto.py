import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Criar o arquivo com 10.000 linhas
num_lines = 10000
line_length = 75

with open('arquivo.txt', 'w') as file:
    for _ in range(num_lines):
        line = generate_random_string(line_length) + '\n'
        file.write(line)
