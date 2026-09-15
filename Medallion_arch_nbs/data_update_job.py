url = 'abfss://gold@adlsolistchurn2026.dfs.core.windows.net/'
catalog = 'olist_ecommerce.default.'

olist_customer = spark.read.format('delta').load(url + 'olist_customers')
olist_customer.write.mode('overwrite').option('overwriteSchema','True').saveAsTable(catalog +'olist_customers')


olist_order_items = spark.read.format('delta').load(url + 'olist_order_items')
olist_order_items.write.mode('overwrite').option('overwriteSchema','True').saveAsTable(catalog +'olist_order_items')

olist_order_payments = spark.read.format('delta').load(url + 'olist_order_payments')
olist_order_payments.write.mode('overwrite').option('overwriteSchema','True').saveAsTable(catalog +'olist_order_payments')

olist_order_reviews = spark.read.format('delta').load(url + 'olist_order_reviews')
olist_order_reviews.write.mode('overwrite').option('overwriteSchema','True').saveAsTable(catalog +'olist_order_reviews')


olist_products = spark.read.format('delta').load(url + 'olist_products')
olist_products.write.mode('overwrite').option('overwriteSchema','True').saveAsTable(catalog +'olist_products')

olist_sellers = spark.read.format('delta').load(url + 'olist_sellers')
olist_sellers.write.mode('overwrite').option('overwriteSchema','True').saveAsTable(catalog +'olist_sellers')

olist_order_records = spark.read.format('delta').load(url + 'olist_order_records')
olist_order_records.write.mode('overwrite').option('overwriteSchema','True').saveAsTable(catalog +'olist_order_records')


