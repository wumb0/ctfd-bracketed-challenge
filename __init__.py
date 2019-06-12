from CTFd.plugins.challenges import BaseChallenge, CHALLENGE_CLASSES
from CTFd.plugins import register_plugin_assets_directory
from CTFd.models import db, Challenges
from flask import Blueprint

class BracketedChallengeType(BaseChallenge):
    id = "bracketed"
    name = "bracketed"
    templates = {
        'create': '/plugins/bracketed_challenges/assets/create.html',
        'update': '/plugins/bracketed_challenges/assets/update.html',
        'view': '/plugins/bracketed_challenges/assets/view.html',
    }
    scripts = {
        'create': '/plugins/bracketed_challenges/assets/create.js',
        'update': '/plugins/bracketed_challenges/assets/update.js',
        'view': '/plugins/bracketed_challenges/assets/view.js',
    }
    route = '/plugins/bracketed_challenges/assets'
    blueprint = Blueprint('bracketed_challenges', __name__, template_folder='templates', static_folder='assets')

    @staticmethod
    def create(request):
        pass

    @staticmethod
    def read(challenge):
        pass

    @staticmethod
    def update(challenge, request):
        pass

    @staticmethod
    def delete(challenge):
        pass

    @staticmethod
    def attempt(challenge, request):
        pass

    @staticmethod
    def solve(user, team, challenge, request):
        pass

    @staticmethod
    def fail(user, team, challenge, request):
        pass


class BracketedChallenge(Challenges):
    __mapper_args__ = {'polymorphic_identity': 'bracketed'}
    id = db.Column(None, db.ForeignKey('challenges.id'), primary_key=True)
    brackets = db.relationship('Brackets', backref='challenges',
                               secondary='challenge_bracket')

cb = db.Table("challenge_bracket",
              db.Column("challenges_id", db.Integer, db.ForeignKey("challenges.id")),
              db.Column("bracket_id", db.Integer, db.ForeignKey("brackets.id"))
              )


def load(app):
    app.db.create_all()
    CHALLENGE_CLASSES['bracketed'] = BracketedChallengeType
    register_plugin_assets_directory(app, base_path='/plugins/bracketed_challenges/assets')
