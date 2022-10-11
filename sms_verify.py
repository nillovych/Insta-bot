from flask import Flask, request, render_template
import datetime
import sqlite3
import sqlite3 as sql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_data():
  if request.method == 'POST':
     number = request.form['from']
     text = request.form['text']
     date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
     if number:
        with sql.connect("messages.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO messages (date,number,text) VALUES (?,?,?)",(date,number,text) )       
        return "Number:{} Text:{}".format(number, text)
     if not number:
        return "No data"
  else:
  		
   		con = sql.connect("messages.db")
   		con.row_factory = sql.Row
   		cur = con.cursor()
   		cur.execute("select * from messages ORDER BY id DESC")
   		rows = cur.fetchall();
   		return render_template('msg.html',rows = rows)


if __name__ == '__main__':
    app.run(debug=True)
