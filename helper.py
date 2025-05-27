from datetime import datetime, timedelta
from database import db

class Item(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    isCompleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Item {self.text} - {self.date}>"

def oneWeekFromToday():
    return datetime.now().date() + timedelta(weeks=1)

def add(text, date=None):
    text = text.replace("b", "bbb").replace("B", "Bbb")

    if date is None:
        date = oneWeekFromToday()
    else:
        date = datetime.strptime(date, "%Y-%m-%d").date()

    item = Item(text=text, date=date)
    db.session.add(item)
    db.session.commit()

def get_all():
    return Item.query.order_by(Item.date).all()

def get(index):
    return get_all()[index]

def update(index):
    item = get(index)
    item.isCompleted = not item.isCompleted
    db.session.commit()

def get_csv():
    import io
    import csv

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["text", "date", "isCompleted"])

    for item in get_all():
        writer.writerow([item.text, item.date.strftime("%Y-%m-%d"), item.isCompleted])

    return output.getvalue()
