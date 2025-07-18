from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # 'visualizador' ou 'editor'
    active = db.Column(db.Boolean, default=True)

    @property
    def is_active(self):
        return self.active

    # Relacionamento com UserObra
    user_obras = db.relationship('UserObra', backref='user', lazy=True)

class Obra(db.Model):
    __tablename__ = 'obra'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    gastos = db.relationship('Gasto', backref='obra', lazy=True)
    obra_users = db.relationship('UserObra', backref='obra', lazy=True)

class Gasto(db.Model):
    __tablename__ = 'gasto'

    id = db.Column(db.Integer, primary_key=True)
    tipo_nota = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data_nota = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    aprovador = db.Column(db.String(100), nullable=False)
    obra_id = db.Column(db.Integer, db.ForeignKey('obra.id'), nullable=False)

class UserObra(db.Model):
    __tablename__ = 'user_obra'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    obra_id = db.Column(db.Integer, db.ForeignKey('obra.id'), nullable=False)
# models.py

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(100))
    tipo = db.Column(db.String(20))  # visualizador, editor, admin
    obras = db.relationship('Obra', secondary='usuario_obra', backref='usuarios')

# Tabela de associação entre usuários e obras
usuario_obra = db.Table('usuario_obra',
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id')),
    db.Column('obra_id', db.Integer, db.ForeignKey('obra.id'))
)
