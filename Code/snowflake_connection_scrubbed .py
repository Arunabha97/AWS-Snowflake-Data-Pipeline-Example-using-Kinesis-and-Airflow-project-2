import snowflake.connector

conn = snowflake.connector.connect(
    user='Your_user_name',
    password='Your_password',
    account='Your_accout_name',
    warehouse='PRO_CURATION',
    database='PRO_DB',
    schema='PUBLIC',
    role='ACCOUNTADMIN'
)
print(conn.cursor().execute("SELECT CURRENT_DATE;").fetchall())
