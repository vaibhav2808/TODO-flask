from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


from dataclasses import dataclass

db = SQLAlchemy()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

@dataclass
class Task(db.Model):
    """Represents a task in the database."""

    id: int
    task: str
    complete: bool
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<Task {self.id}>'




@app.route('/tasks', methods=['POST'])
def create_task():
    """Creates a new task."""
    task = request.json.get('task', '')
    if not task:
        return jsonify({'message': 'Task name required'}), 400

    complete = False

    new_task = Task(task=task, complete=complete)
    db.session.add(new_task)
    db.session.commit()

    response = {
        'id': new_task.id,
        'task': new_task.task,
        'complete': new_task.complete
    }

    return jsonify(response)

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """Deletes a task with the given ID."""
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    response = {
        'id': id,
        'message': 'Task deleted successfully'
    }

    return jsonify(response)

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """Updates a task with the given ID."""
    task = Task.query.get_or_404(id)

    task.task = request.json.get('task', task.task)
    task.complete = request.json.get('complete', task.complete)

    db.session.commit()

    response = {
        'id': id,
        'task': task.task,
        'complete': task.complete
    }

    return jsonify(response)

@app.route('/tasks/<int:id>/complete', methods=['PUT'])
def mark_complete(id):
    """Marks a task as complete with the given ID."""
    task = Task.query.get_or_404(id)

    task.complete = True
    db.session.commit()

    response = {
        'id': id,
        'message': 'Task marked as complete'
    }

    return jsonify(response)

@app.route('/tasks/<int:id>/incomplete', methods=['PUT'])
def mark_incomplete(id):
    """Marks a task as incomplete with the given ID."""
    task = Task.query.get_or_404(id)

    task.complete = False
    db.session.commit()

    response = {
        'id': id,
        'message': 'Task marked as incomplete'
    }

    return jsonify(response)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Returns all tasks."""
    tasks = Task.query.all()
    response = {
        'tasks': tasks
    }

    return jsonify(response)

@app.route('/tasks/<int:id>/toggle', methods=['PUT'])
def toggle_task(id):
    """Toggles a task with the given ID."""
    task = Task.query.get_or_404(id)
    task.complete = not task.complete
    db.session.commit()

    response = {
        'id': id,
        'message': 'Task toggled successfully'
    }
    return jsonify(response)

    # Error handling routes
@app.errorhandler(400)
def bad_request(e):
    return jsonify({'message': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
     with app.app_context():
        db.init_app(app)
        db.create_all()
        app.run(debug=True)
