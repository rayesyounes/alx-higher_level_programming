#!/usr/bin/python3
"""states models"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    port = 3306

    query = "SELECT name FROM cities WHERE state_id IN \
            (SELECT id FROM states WHERE name LIKE BINARY %s) ORDER BY cities.id ASC"
    params = (state_name,)

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    cursor = db.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
