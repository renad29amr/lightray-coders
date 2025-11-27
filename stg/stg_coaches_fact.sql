{{config(materialized='table',
        constraints=[
            {'type':'primary_key','columns':['coach_id']}
        ])}}

SELECT
    coach_id,
    Manager as coach_name,
    Nationality as nationality,
    Club as club, 
    strftime(strptime(Appointed, '%d-%b-%y'), '%d/%m/%y') as appointment_date,
    "Time as manager" as time_as_years,
    "Salary (million)" as salary_in_millions

FROM {{ ref('cleaned_coaches') }}
