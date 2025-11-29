{{ config(materialized='table') }}

SELECT
    gk_id,
    gk,
    nation,
    club,
    age
FROM {{ ref('stg_gk') }}