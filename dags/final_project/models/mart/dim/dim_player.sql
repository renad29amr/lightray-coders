{{ config(materialized='table') }}


SELECT
    player_id,
    player,
    nation,
    club,
    age,
    position
FROM {{ ref('stg_player') }}