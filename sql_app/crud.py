from sqlalchemy.orm import Session, selectinload

import models as models
import schemas as schemas
"""from . import models, schemas"""

def get_match(db: Session, match_id: int):
    return schemas.Game.from_orm(db.query(models.Game).options(selectinload(models.Game.playerstats)).filter(models.Game.id == match_id).first())


def get_hero(db: Session, hero_id: int):
    print(1)
    return db.query(models.HeroInfo).filter(models.HeroInfo.id == hero_id).first()


def get_matchs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).order_by(models.Game.id.desc()).offset(skip).limit(limit).all()

def get_matchs_by_league_id(db: Session, league_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Game).filter(models.Game.league_id == league_id).offset(skip).limit(limit).all()

def create_match(db: Session, game: schemas.GameCreate):

    #fake_hashed_password = user.password + "notreallyhashed"
    db_new_game = models.Game(id=game.id, league_id=game.league_id, radiant_score=game.radiant_score, dire_score=game.dire_score, duration=game.duration, is_valid=game.is_valid)
    db.add(db_new_game)
    db.commit()
    db.refresh(db_new_game)
    return db_new_game


def get_playerstats(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PlayerStat).offset(skip).limit(limit).all()

def get_playerstats_for_specific_match(db: Session, match_id: int):
    return db.query(models.PlayerStat).order_by(models.PlayerStat.slot.asc()).filter(models.PlayerStat.match_id == match_id).all()


def create_playerstats_for_game(db: Session, playerstats: schemas.PlayerStatCreate, match_id: int):
    db_new_playerstats = models.PlayerStat(match_id=match_id, slot=playerstats.slot, hero_id=playerstats.hero_id, num_kills=playerstats.num_kills, isRadiant=playerstats.isRadiant)
    #Item(**playerstats.dict(), match_id=match_id)
    db.add(db_new_playerstats)
    db.commit()
    db.refresh(db_new_playerstats)
    return db_new_playerstats
