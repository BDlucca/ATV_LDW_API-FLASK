from .database import db

class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, default="Ativo")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Pedido(db.Model):
    __tablename__ = 'pedido'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)

    # Relacionamento: um hotel tem várias reservas
    # bookings = db.relationship('Booking', backref='hotel', cascade='all, delete-orphan')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Produto(db.Model):
    __tablename__ = 'Produto'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    total_pagar = db.Column(db.Float)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}