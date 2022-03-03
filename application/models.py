from application import db

class Project(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    project_name = db.Column(db.String(30))
    due_date = db.Column(db.Date)
    proj_items = db.relationship('Todo', backref='project')
    def __str__(self):
         return f"{self.pk} {self.project_name} {self.due_date}"

class Todo(db.Model):
    pk = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30))
    desc = db.Column(db.String(100))
    status = db.Column(db.String(4))
    proj_id = db.Column(db.Integer, db.ForeignKey('project.pk'))
    def __str__(self):
        return f"{self.pk} {self.status} {self.title}:\n{self.desc}"

