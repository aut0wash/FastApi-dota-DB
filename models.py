from datetime import datetime
from config import db, ma

class Hero(db.Model):
    __tablename__ = 'hero'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    displayname = db.Column(db.String, nullable=False)
    uri = db.Column(db.String, nullable=False)
    main_attribute = (db.String, nullable=False)
    difficulty = (db.Integer, default=0)
    attack_type = (db.String, default='')
    url_icon_sg = db.Column(db.Text, nullable=False)
    url_icon_lg = db.Column(db.Text, nullable=False)
    url_icon_full = db.Column(db.Text, nullable=False)
    url_icon_vert = db.Column(db.Text, nullable=False)
    url_icon_minimap = db.Column(db.Text, nullable=False)

class HeroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hero
        sqla_session = db.session
        load_instance = True


class Npc(db.Model):
    __tablename__="npc"
    pknpc = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.Enum('hero', 'unit'), nullable=False)

class NpcSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Npc
        sqla_session = db.session
        load_instance = True


class Item(db.Model):
    __tablename__="item"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    displayname= cb.Column(db.String, nullable=False)
    uri = db.Column(db.String, nullable=False)
    is_support_ful_item = db.Column(db.String, default='')
    behavior = db.Column(db.Integer, default=None)
    unit_target_type = db.Column(db.Integer, default=None)
    unit_target_team = db.Column(db.Integer, default=None)
    unit_target_flags = db.Column(db.Integer, default=None)
    flight_level_recap = db.Column(db.Integer, default=None)
    castrange = db.Column(db.Integer, default=None)
    castpoint = db.Column(db.Integer, default=None)
    cooldwon = db.Column(db.Integer, default=None)
    manacost = db.Column(db.Integer, default=None)
    channeltime = db.Column(db.Integer, default=None)
    shared_cooldown = db.Column(db.Integer, default=None)
    cost = db.Column(db.Integer, default=None)
    shoptags = db.Column(db.String, default=None)
    aliases = db.Column(db.String, default=None)
    quality = db.Column(db.String, default=None)
    is_sellable = db.Column(db.String, default=None)
    is_stackable = db.Column(db.String, default=None)
    is_permanent = db.Column(db.String, default=None)
    is_hide_charges = db.Column(db.String, default=None)
    requires_charges = db.Column(db.String, default=None)
    is_support = db.Column(db.String, default=None)
    is_alertable = db.Column(db.String, default=None)
    is_tempest_double_clonable = db.Column(db.String, default=None)
    stockmax = db.Column(db.Integer, default=None)
    initialcharges = db.Column(db.Integer, default=None)
    initialstock = db.Column(db.Integer, default=None)
    stocktime = db.Column(db.Integer, default=None)
    initialstock_time = db.Column(db.Integer, default=None)
    is_recipe = db.Column(db.String, default=None)
    description = db.Column(db.Text, default=None)
    notes = db.Column(db.Text, default=None)
    attributes = db.Column(db.Text, default=None)
    lore = attributes = db.Column(db.Text, default=None)
    needs_components = db.Column(db.String, default=None)
    is_full_item_hero_purchase_item = db.Column(db.String, default=None)
    url_icon = db.Column(db.Text, default=None)

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        sqla_session = db.session
        load_instance = True


class League(db.Model):
    __tablename__ = 'league'
    league_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    league_name = db.Column(db.Text, nullable=False)
    league_tag = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    is_ftv = db.Column(db.Integer, default=0)
    parse_it = db.Column(db.Integer, default=0)
    post_it = db.Column(db.Integer, default=0)

class LeagueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = League
        sqla_session = db.session
        load_instance = True


class Team(db.Model):
    __tablename__ = 'team'
    team_id = db.Column(db.Integer, primary_key=True, nullable=False)
    team_name = db.Column(db.Text, nullable=False)
    team_name_canonical = db.Column(db.Text, nullable=False)
    team_tag = db.Column(db.Text, nullable=False)
    logo_url = db.Column(db.Text, nullable=False)
    in_ftv_league = db.Column(db.Integer, default=0)

class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team
        sqla_session = db.session
        load_instance = True


class User(db.Model):
    __tablename__ = 'user'
    discord_id = db.Column(db.Integer, primary_key=True, nullable=False)
    discord_name = db.Column(db.Text, nullable=False)
    discord_role = db.Column(db.Integer, default=0)
    is_owner = db.Column(db.Integer, default=0)
    is_admin = db.Column(db.Integer, default=0)
    is_caster = db.Column(db.Integer, default=0)
    is_player = db.Column(db.Integer, default=0)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True


class GameAcquired(db.Model):
    __tablename__ = 'game_acquired'

class GameAcquiredSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GameAcquired
        sqla_session = db.session
        load_instance = True
