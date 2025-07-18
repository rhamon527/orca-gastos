from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# Associação entre usuários e obras (relacionamento muitos-para-muitos)
user_obras = db.Table('user_obras',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('obra_id', db.Integer, db.ForeignKey('obra.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    active = db.Column(db.Boolean, default=True)

    @property
    def is_active(self):
        return self.active

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # 'visualizador' ou 'editor'

    # Obras que o usuário pode acessar
    obras = db.relationship('Obra', secondary=user_obras, backref='usuarios')

class Obra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    gastos = db.relationship('Gasto', backref='obra', lazy=True)

class Gasto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_nota = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data_nota = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    aprovador = db.Column(db.String(100), nullable=False)
    obra_id = db.Column(db.Integer, db.ForeignKey('obra.id'), nullable=False)
