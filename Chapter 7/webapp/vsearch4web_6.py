import html
import mysql.connector

from flask import Flask, render_template, request, escape
from vsearch import search4letters as s4l

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    dbconfig = {'host': '127.0.0.1', 'user': 'vsearch', 'database': 'vsearchlogDB',}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    _SQL = """insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res, ))
    conn.commit()

    cursor.close()
    conn.close()


@app.route('/search4', methods=['POST'])
def do_search() -> html:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results:"
    results = s4l(phrase, letters)
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
def view_the_log() -> 'html':
    contests = []
    with open('vsearch.log') as log:
        for string in log:
            contests.append([])
            for item in string.split('|'):
                contests[-1].append(escape(item))

    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contests,)


if __name__ == '__main__':
    app.run(debug=True)
