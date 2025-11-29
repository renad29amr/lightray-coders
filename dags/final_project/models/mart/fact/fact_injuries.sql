{{ config(materialized='table') }}

SELECT
    MD5(LOWER(TRIM(i.player)) || i.club ) AS injury_fact_id,
    p.player_id,
    i.club,
    i.injury_type,
    i.return_date
FROM {{ ref('stg_injuries') }} AS i
LEFT JOIN {{ ref('dim_player') }} AS p
ON i.player = p.player
LEFT JOIN {{ref('dim_club')}} c
on c.club = i.club
