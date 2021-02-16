from typing import List, Optional

from pydantic import BaseModel

class HeroStatBase(BaseModel):
    hero_id: int
    hero_name : str

    class Config:
        orm_mode = True

class PlayerStatBase(BaseModel):
    slot: int
    hero_id: int
    num_kills: int
    isRadiant: bool

    class Config:
        orm_mode = True


class PlayerStatCreate(PlayerStatBase):
    pass

    class Config:
        orm_mode = True


class PlayerStat(PlayerStatBase):
    slot: int
    hero_id: int
    num_kills: int
    isRadiant: bool

    class Config:
        orm_mode = True

class GameBase(BaseModel):
    id: int
    league_id: int
    radiant_score: int
    dire_score: int
    duration: int
    is_valid: bool

    class Config:
        orm_mode = True


class GameCreate(GameBase):
    pass

    class Config:
        orm_mode = True


class Game(GameBase):
    id: int
    league_id: int
    radiant_score: int
    dire_score: int
    duration: int
    is_valid: bool
    playerstats: List[PlayerStat] = [{}]

    class Config:
        orm_mode = True
