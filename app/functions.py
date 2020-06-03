from app import db
from models import Record


def freetime():
    records = Record.query.all()
    time = [str(i) + '.00' for i in range(10, 21)]
    for record in records:
        if record.time in time:
            time.remove(record.time)
    freetime = []
    for i in time:
        freetime.append((i))
    return time