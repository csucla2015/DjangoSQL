import pymssql
conn = pymssql.connect(server='fejcz4m54q.database.windows.net', user='meet_bhagdev@fejcz4m54q', password='channelV1', database='meet_bhagdev')
cursor = conn.cursor()
cursor.execute("""
IF OBJECT_ID('votes', 'U') IS NOT NULL
    DROP TABLE votes
CREATE TABLE votes (
    name VARCHAR(100),
    value INT NOT NULL,
    PRIMARY KEY(name)
)
""")
cursor.executemany(
    "INSERT INTO votes VALUES (%s, %d)",
    [('NodeJS', '0'),
     ('Python', '0'),
     ('C#', '0')])
# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()
