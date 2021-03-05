from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class HeroInfo(Base):
    __tablename__ = "herosinfos"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    playerstats = relationship("PlayerStat", back_populates="heroinfos")


class ItemInfo(Base):
    __tablename__ = "itemsinfos"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    patch = Column(Integer, primary_key=True)

    playerstats = relationship("PlayerStat", back_populates="itemsinfos")
    game = relationship("Game", back_populates="itemsinfos")


class PlayerStat(Base):
    __tablename__ = "playerstats"

    match_id = Column(Integer, ForeignKey("games.id"), primary_key=True)
    slot = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey("herosinfos.id"), primary_key=True)
    num_kills = Column(Integer, default=None)
    isRadiant = Column(Boolean, default=None)
    item_0 = Column(Integer, ForeignKey("itemsinfos.id"))


    game = relationship("Game", back_populates="playerstats")
    heroinfos = relationship("HeroInfo", back_populates="playerstats", lazy="joined")
    itemsinfos = relationship("ItemInfo", back_populates="playerstats", lazy="joined")


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    league_id = Column(Integer)
    patch = Column(Integer, ForeignKey("itemsinfos.patch"))
    radiant_score = Column(Integer)
    dire_score = Column(Integer)
    duration = Column(Integer)
    is_valid = Column(Boolean, default=True)

    playerstats = relationship("PlayerStat", back_populates="game", lazy="joined", order_by='asc(PlayerStat.slot)')
    itemsinfos = relationship("ItemInfo", back_populates="game", lazy="joined")
