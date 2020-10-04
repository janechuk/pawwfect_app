"""Seed file for adoption agency app"""
from models import Pet, db
from app import app



#creat all tables
db.drop_all()
db.create_all()


p1 = Pet(name="Snargle", species="cat", photo_url="https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60", age=3, notes="What do dogs do on their day off? Can't lie around—that's their job.", available=True)
p2 = Pet(name="Porcheta", species="cat", photo_url="https://images.unsplash.com/photo-1539641388297-277284b9ba67?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60", age=2, notes="No matter how you’re feeling, a little dog gonna love you", available=True)
p3 = Pet(name="Bosco", species="dog", photo_url="https://images.unsplash.com/flagged/photo-1583958211970-af3e1596ef32?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60", age=4, notes="When the dog looks at you, the dog is not thinking what kind of a person you are. The dog is not judging you.", available=False)
p4 = Pet(name="Chewy", species="dog", photo_url="https://images.unsplash.com/photo-1576944184764-3186cba58d31?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60", age=1, notes="If you pick up a starving dog and make him prosperous he will not bite you. This is the principal difference between a dog and man", available=True)
p5 = Pet(name="Shibly", species="cat", photo_url="https://images.unsplash.com/photo-1544568100-847a948585b9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60", age=3, notes="What do dogs do on their day off? Can't lie around—that's their job.", available=True)
p6 = Pet(name="Luly", species="cat", photo_url="https://images.unsplash.com/photo-1527526029430-319f10814151?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60", age=2, notes="No matter how you’re feeling, a little dog gonna love you", available=True)
p7 = Pet(name="Howgdy", species="dog", photo_url="https://images.unsplash.com/flagged/photo-1583958211970-af3e1596ef32?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60", age=4, notes="When the dog looks at you, the dog is not thinking what kind of a person you are. The dog is not judging you.", available=False)
p8 = Pet(name="Pascal", species="dog", photo_url="https://images.unsplash.com/photo-1566489564594-f2163930c034?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60", age=1, notes="If you pick up a starving dog and make him prosperous he will not bite you. This is the principal difference between a dog and man", available=True)


db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8])
db.session.commit()