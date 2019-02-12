from db import db

class library_model(db.Model):


    __tablename__ = 'library'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    email =  db.Column(db.String(100))
    owner_name = db.Column(db.String(100))
    owner_email = db.Column(db.String(100))
    rating = db.Column(db.Integer)



    def __init__(self, name,location,email,owner_name,owner_email,rating):
        self.name = name
        self.location = location
        self.email = email
        self.owner_name = owner_name
        self.owner_email = owner_email
        self.rating = rating



    @classmethod
    def get_all_library_list(cls):
        lib_list = []
        all_libarry = db.session.query(cls).all()
        for row in all_libarry:
            lib_list.append(cls(row.name,row.location,row.email,row.owner_name,row.owner_email,row.rating))
        return lib_list



    @classmethod
    def save_libarary_info(cls,data):
        db.session.add(cls(data['name'],
                                   data['location'],
                                   data['email'],
                                   data['owner_name'],
                                   data['owner_email'],
                                   data['rating']))
        db.session.commit()

        return {'Status':'Successful'} , 201



    @classmethod
    def update_library_info(cls , data):
        library_data = db.session.query(cls).filter_by(email = data['email']).first()
        library_data.name = data['name']
        library_data.location = data['location']
        library_data.owner_name = data['owner_name']
        library_data.owner_email = data['owner_email']
        library_data.rating = data['rating']

        db.session.commit()

        return {'Status':'Successful'} , 201



    @classmethod
    def delete_library_info(cls,data):

        library_data = db.session.query(cls).filter_by(email = data['email']).first()
        db.session.delete(library_data)
        db.session.commit()

        return {'Status':'Successful'} , 201


