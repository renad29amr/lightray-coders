{{ config(materialized='table') }}

SELECT
    m.match_id,
    m.match_date,
  
    dclub_home.club_id AS home_club_id,
    dclub_home.club AS home_club_name,
    dclub_away.club_id AS away_club_id,
    dclub_away.club AS away_club_name,

    m.ft_home_goals,
    m.ft_away_goals,
    m.ft_result,
    m.ht_home_goals,
    m.ht_away_goals,
    m.ht_result,
    m.home_shots,
    m.away_shots,
    m.home_shots_on_target,
    m.away_shots_on_target,
    m.home_corners,
    m.away_corners,
    m.home_fouls,
    m.away_fouls,
    m.home_yellow,
    m.away_yellow,
    m.home_red,
    m.away_red

FROM {{ ref('stg_match') }} AS m

LEFT JOIN {{ ref('dim_club') }} AS dclub_home
    ON LOWER(TRIM(m.home_team)) = LOWER(TRIM(dclub_home.club))

LEFT JOIN {{ ref('dim_club') }} AS dclub_away
    ON LOWER(TRIM(m.away_team)) = LOWER(TRIM(dclub_away.club))
