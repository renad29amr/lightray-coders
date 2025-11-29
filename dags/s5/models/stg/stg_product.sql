{{config(materialized='table',
        constraints=[
            {'type': 'foreign_key', 'columns': ['category_id'], 'references': {'table': 'stg_category', 'columns': ['id']}}
        ])}}
select 
    id, 
    title,
    slug,
    price,
    description,
    creationAt,
    updatedAt,
    (category).id as category_id

from {{ source('raw','raw_products') }}