from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

import models as models

SQLALCHEMY_DATABASE_URL = "sqlite:///./dotaleague.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Session = sessionmaker(bind = engine)
session = Session()


match_id =1

game = session.query(models.Game).filter(models.Game.id == match_id).all()

attrs = vars(game[0].itemsinfos)
print(', '.join("%s: %s" % item for item in attrs.items()))


"""print(game.league_id)
print(game.playerstats[0].slot)
print(game.playerstats[0].heroinfos.name)
print(game.playerstats[0].hero_id)
print(game.playerstats[1].slot)
print(game.playerstats[1].heroinfos.name)
print(game.playerstats[1].hero_id)
print(game.playerstats[0].itemsinfos.id)
print(game.playerstats[0].itemsinfos.name)
print(game.playerstats[0].itemsinfos.patch)

attrs = vars(game.playerstats[0].itemsinfos)
print(', '.join("%s: %s" % item for item in attrs.items()))

#game = session.query(models.Game, models.PlayerStat, models.HeroInfo).join(models.Game.playerstats).join(models.HeroInfo, models.HeroInfo.id == models.PlayerStat.hero_id).filter(models.Game.id == match_id).all()


print("playerstats")
pl = session.query(models.PlayerStat).filter(models.PlayerStat.hero_id == 14).one()
print(pl.hero_id)
print(pl.heroinfos.name)

print('test')
p = session.query(models.PlayerStat).order_by(models.PlayerStat.slot.asc()).filter(models.PlayerStat.match_id == match_id).all()
print(p)
print(p[0].hero_id, p[0].heroinfos.name)
print("le game id est", p[0].game.id)

attrs = vars(p[0])
print(', '.join("%s: %s" % item for item in attrs.items()))
"""
