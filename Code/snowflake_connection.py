import snowflake.connector

conn = snowflake.connector.connect(
    user='Arunabha1997',
    password='Ray@1997',
    account='wwfenru-ktb44415',
    warehouse='PRO_CURATION',
    database='PRO_DB',
    schema='PUBLIC',
    role='ACCOUNTADMIN'
)
print(conn.cursor().execute("SELECT CURRENT_DATE;").fetchall())
