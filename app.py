from flask import Flask, render_template, request
import sqlite3, os.path

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def Choose_list():
    return render_template('Choose_list.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    result_l = []
    if request.method == 'POST':
        choose_list = request.form
        c_list = choose_list['list'].split(',')
        for l in c_list:
            result = sql_mod(l)
            result_l.append({'number':l,
                             'words': result
                             })
    return render_template('index.html',
                           choose_list = result_l)

def sql_mod(table_name):
    value_list = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "3k.sqlite")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cursor = cur.execute('SELECT Column1, Column2 FROM list'+table_name)
    for row in cursor:
        value_list.append(list(row))
    conn.close()
    return value_list

if __name__ == '__main__':
    app.run()
