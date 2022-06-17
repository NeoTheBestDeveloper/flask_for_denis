from flask import Flask, render_template

app = Flask(__name__)

polls = [
    {
        'title': 'Cool post 1',
        'content': 'Cool post 1 content',
        'author': 'Aboba'
    },
    {
        'title': 'Cool post 2',
        'content': 'babajuy',
        'author': 'zxc gool'
    },
]

menu = (('get_polls', 'Polls'), )


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', menu=menu)


@app.route('/polls', methods=['GET'])
def get_polls():
    return render_template('polls.html', polls=polls)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
