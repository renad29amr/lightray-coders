{{ config(materialized='table') }}

SELECT
    match_id,
    MatchDate AS match_date,
    HomeTeam AS home_team,
    AwayTeam AS away_team,
    FullTimeHomeGoals AS ft_home_goals,
    FullTimeAwayGoals AS ft_away_goals,
    FullTimeResult AS ft_result,
    HalfTimeHomeGoals AS ht_home_goals,
    HalfTimeAwayGoals AS ht_away_goals,
    HalfTimeResult AS ht_result,
    HomeShots AS home_shots,
    AwayShots AS away_shots,
    HomeShotsOnTarget AS home_shots_on_target,
    AwayShotsOnTarget AS away_shots_on_target,
    HomeCorners AS home_corners,
    AwayCorners AS away_corners,
    HomeFouls AS home_fouls,
    AwayFouls AS away_fouls,
    HomeYellowCards AS home_yellow,
    AwayYellowCards AS away_yellow,
    HomeRedCards AS home_red,
    AwayRedCards AS away_red

FROM {{ ref('cleaned_match') }}