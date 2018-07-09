from sqlalchemy.ext.associationproxy import association_proxy
from app import db


recipe_ingreds = db.Table('recipe_ingreds',
                db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
                db.Column('ingred_id', db.Integer, db.ForeignKey('ingredient.id')))

creature_recipe = db.Table('creature_recipe',
                db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
                db.Column('creature_id', db.Integer, db.ForeignKey('creature.id')))



class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    rating = db.Column(db.String(12), unique=True)

    ingredients = db.relationship("Ingredient",
                                  secondary=recipe_ingreds)
    ingredient_name = association_proxy('ingredient', 'name')


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)


class Creature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    type = db.Column(db.String(25))
    recipe = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    best_recipe = db.relationship('Recipe', backref='creature', lazy=True)

