import random

def get_random_template(category='friends'):
    with open(f'templates/{category}.txt', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return random.choice(lines)