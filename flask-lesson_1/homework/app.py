from flask import Flask, render_template, request, url_for, abort
from werkzeug.utils import redirect

app = Flask(__name__)


fruits_list = ['apple', 'banana', 'orange',]
vegetables_list = ['potato', 'tomato', 'cucumber']


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/')
def redirect_to_main():
    return redirect(url_for('main'))


@app.route('/fruits')
@app.route('/fruits/<string:value>', methods=['GET', 'POST', 'DELETE'])
def fruits(value=None):
    if request.method == 'POST':
        do_post_fruit(value)
        return f"Now we have {value}"
    if request.method == 'DELETE':
        if value not in vegetables_list:
            return abort(404)
        else:
            do_delete_vegetable(value)
            return "We still have a couple"
    else:
        return do_get_fruit()


def do_get_fruit():
    return render_template('fruits.html', fruits_list=fruits_list)


def do_delete_fruit(value):
    fruits_list.remove(value)


def do_post_fruit(value):
    fruits_list.append(value)


@app.route('/vegetables')
@app.route('/vegetables/<string:value>', methods=['GET', 'POST', 'DELETE'])
def vegetables(value=None):
    if request.method == 'POST':
        do_post_vegetable(value)
        return f"Now we have {value}"
    if request.method == 'DELETE':
        if value not in vegetables_list:
            return abort(404)
        else:
            do_delete_vegetable(value)
            return "We still have a couple"
    else:
        return do_get_vegetable()


def do_get_vegetable():
    return render_template('vegetables.html', vegetables_list=vegetables_list)


def do_delete_vegetable(value):
    vegetables_list.remove(value)


def do_post_vegetable(value):
    vegetables_list.append(value)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
