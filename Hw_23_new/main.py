from flask import Flask, request
import os.path
from utils import get_filter, get_map, get_unique, get_sort, get_limit


app = Flask(__name__)


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Hw_23_new/data')


def apply_filter(data_path):
    choice_func = {
        'filter': get_filter,
        'map': get_map,
        'unique': get_unique,
        'sort': get_sort,
        'limit': get_limit
    }

    with open(data_path) as file:
        data = file.readlines()

    for item in request.form:
        if item[0:3] == 'cmd':
            func = choice_func[request.form[item]]
            num_cmd = item[3]
            key_value = 'value' + num_cmd
            value = request.form.get(key_value)
            data = func(data, value)

    return data


@app.route('/perform_query', methods=['POST'])
def perform_query():
    file_name = request.form.get('file_name')

    if file_name:
        data_path = os.path.join(BASE_DIR, file_name)
    else:
        return f'файл {file_name} не найден', 400

    if not os.path.isfile(data_path):
        return f'файл {file_name} не найден', 400

    return app.response_class(apply_filter(data_path), content_type="text/plain")


if __name__ == '__main__':
    app.run()
