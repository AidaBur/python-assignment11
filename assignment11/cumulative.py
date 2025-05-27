import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("../../python_homework/db/lesson.db")

query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

df = pd.read_sql_query(query, conn)
conn.close()

df["cumulative"] = df["total_price"].cumsum()

df.plot(kind="line", x="order_id", y="cumulative", title="Cumulative Revenue Over Orders")

plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.tight_layout()
plt.show()
