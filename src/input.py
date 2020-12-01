import os


def get_input_filename(day):
    return os.path.join(
        os.path.dirname(__file__), '..', 'data', f'day{day}.txt')
