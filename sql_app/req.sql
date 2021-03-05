SELECT
    games.id AS games_id,
    games.league_id AS games_league_id,
    games.patch AS games_patch,
    games.radiant_score AS games_radiant_score,
    games.dire_score AS games_dire_score,
    games.duration AS games_duration,
    games.is_valid AS games_is_valid,
    playerstats.match_id AS playerstats_1_match_id,
    playerstats.slot AS playerstats_1_slot,
    playerstats.hero_id AS playerstats_1_hero_id,
    herosinfos_1.id AS herosinfos_1_id,
    herosinfos_1.name AS herosinfos_1_name,
    playerstats.item_0 AS playerstats_item_0,
    itemsinfos.id AS itemsinfos_1_id,
    itemsinfos.name AS itemsinfos_1_name,
    itemsinfos.patch AS itemsinfos_1_patch,
    playerstats.num_kills AS playerstats_1_num_kills,
    playerstats."isRadiant" AS "playerstats_1_isRadiant"
FROM
    games
    JOIN itemsinfos ON itemsinfos.patch = games.patch
    AND itemsinfos.id = playerstats.item_0
    JOIN playerstats AS playerstats ON games.id = playerstats.match_id
    JOIN herosinfos AS herosinfos_1 ON herosinfos_1.id = playerstats.hero_id
WHERE
    games.id = 1 and itemsinfos.patch = games.patch and playerstats.slot=0
ORDER BY
    playerstats.slot ASC
