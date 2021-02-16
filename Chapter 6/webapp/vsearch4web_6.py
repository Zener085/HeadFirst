import html
from flask import Flask, render_template, request
from vsearch import search4letters as s4l

app = Flask(__name__)


def log_request(req, res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req, res, file=log)


@app.route('/search4', methods=['POST'])
def do_search() -> html:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results:"
    results = s4l(phrase, letters)
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_result=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> html:
    return render_template('entry.html', name='name',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contests = log.read()
        return contests


if __name__ == '__main__':
    app.run(debug=True)
