from main import db, Query

all_messages = Query.query.get(2)

db.session.delete(all_messages)
db.session.commit()