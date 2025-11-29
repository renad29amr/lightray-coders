{{config(materialized='table',
        constraints=[
            {'type':'primary_key','columns':['id']}
        ])}}
        
select distinct
    (category).id         as id,
    (category).name       as name,
    (category).slug       as slug,
    (category).creationAt as creationAt,
    (category).updatedAt  as updatedAt

from {{ source('raw','raw_products') }}