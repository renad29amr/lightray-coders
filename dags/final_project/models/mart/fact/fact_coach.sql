{{ config(materialized='table') }}
SELECT
    c.coach_id,
    c.coach,
    c.nationality,
    c.club,
    c.appointment_date,
    c.time_as_years,
    c.salary_in_millions
FROM {{ref("stg_coach")}} c
LEFT JOIN {{ref('dim_club')}} dc
on c.club = dc.club