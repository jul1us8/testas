from main import db, Query

db.create_all()

jonas = Query("Jonas", "jonas@gmail.com", "Labai geras zmogus")
juozas = Query("Juozas", "juozas@gmail.com", "Labai normalus zmogus")
petras = Query("Petras", "petras@gmail.com", "Labai blogas zmogus")

db.session.add_all([jonas, juozas, petras])
db.session.commit()

print(jonas.id)
print(juozas.id)
print(petras.id)