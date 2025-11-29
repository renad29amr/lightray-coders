select
    c.name,
    count(*) as product_count,
    avg(p.price) as avg_price 
from {{ref('stg_product')}} as p join 
{{ref('stg_category')}} as c
on p.category_id = c.id

group by p.category_id, c.name


