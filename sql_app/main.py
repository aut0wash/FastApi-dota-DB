from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud as crud
import models as models
import schemas as schemas
"""from . import crud, models, schemas"""
from database import SessionLocal, engine

#models.Base.metadata.create_all(bind=engine)
#

"""uvicorn main:app --reload"""

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/matches/", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    db_game = crud.get_match(db, match_id=game.id)
    if db_game:
        raise HTTPException(status_code=400, detail="Game already parsed")
    print(game)
    return crud.create_match(db=db, game=game)


@app.get("/matches/", response_model=List[schemas.Game])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    matchs = crud.get_matchs(db, skip=skip, limit=limit)
    return matchs


@app.get("/matches/{match_id}", response_model=schemas.Game)
def read_game(match_id: int, db: Session = Depends(get_db)):
    db_game = crud.get_match(db, match_id=match_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game

@app.get("/matches/{match_id}/players", response_model=List[schemas.PlayerStat])
def read_playerstats_from_a_game(match_id: int, db: Session = Depends(get_db)):
    print(match_id)
    players_stats = crud.get_playerstats_for_specific_match(db, match_id=match_id)
    print(players_stats)
    if players_stats is None:
        raise HTTPException(status_code=404, detail="Stats not found for this game")

    return players_stats


@app.post("/matches/{match_id}/players/", response_model=schemas.PlayerStat)
def create_player_for_game(
    match_id: int, playerstats: schemas.PlayerStatCreate, db: Session = Depends(get_db)
):
    return crud.create_playerstats_for_game(db=db, playerstats=playerstats, match_id=match_id)


@app.get("/players/", response_model=List[schemas.PlayerStat])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    playerstats = crud.get_playerstats(db, skip=skip, limit=limit)
    return playerstats
