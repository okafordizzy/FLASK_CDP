
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)


#finding the current app path. (location of this file)
project_dir = os.path.dirname(os.path.abspath(__file__))

#creating the database file (list.db) to the sqlalchemy dependency
database_file = "sqlite:///{}".format(os.path.join(project_dir, "list.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    todo= db.Column(db.String(100), unique=False, nullable=False, primary_key=True)

    def __repr__(Self):
        return f"Todo: {self.todo}"
        #return "Todo: {}". format(self.todo)
    


"""
todoData = []


@app.route('/')
def index():
    return render_template("index.html", todos=todoData)

@app.route('/create_todo', methods=["POST"])
def create_todo():
    new_todo = request.form.get("new_todo")
    todoData.append(new_todo)
    return redirect(url_for("index"))
 
@app.route("/delete_todo/<todo_item>")
def delete(todo_item):
    todoData.remove(todo_item)
    return redirect(url_for("index"))

index_to_update=''
@app.route("/Update/<todo_item>")
def update(todo_item):
    global index_to_update
    index_to_update = todoData.index(todo_item)
    return render_template('update.html', todo_item=todo_item)

@app.route("/Update_item", methods= ['POST'])
def update_item():

    if request.method == 'POST':

        new_item = request.form.get('new_item')
        todoData[index_to_update] = new_item

        return redirect(url_for('index'))

"""

if __name__=='__main__':
    app.run(debug=True)

