from scripts.transform.sales import new_sales_data
from datetime import datetime

updated_at = datetime.now()
data = new_sales_data(updated_at)
print(data)
