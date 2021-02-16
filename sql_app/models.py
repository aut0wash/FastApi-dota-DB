from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    league_id = Column(Integer)
    radiant_score = Column(Integer)
    dire_score = Column(Integer)
    duration = Column(Integer)
    is_valid = Column(Boolean, default=True)

    playerstats = relationship("PlayerStat", back_populates="match", lazy="selectin", order_by='asc(PlayerStat.slot)')


class PlayerStat(Base):
    __tablename__ = "playerstats"

    match_id = Column(Integer, ForeignKey("games.id"), primary_key=True)
    slot = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey("heros.id"))
    num_kills = Column(Integer, default=None)
    isRadiant = Column(Boolean, default=None)


    match = relationship("Game", back_populates="playerstats", lazy="selectin")
    heros = relationship("Hero", back_populates="playerstats", lazy="selectin")

class Hero(Base):
    __tablename__ = "heros"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    playerstats = relationship("PlayerStat", back_populates="heros", lazy="selectin")
