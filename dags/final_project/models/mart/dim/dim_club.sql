{{ config(materialized='table') }}

WITH base AS (
    SELECT
        DISTINCT
        club,
        club_url
    FROM {{ ref('stg_club') }}
)

SELECT
    ROW_NUMBER() OVER (ORDER BY club) AS club_id,
    club,
    club_url
FROM base