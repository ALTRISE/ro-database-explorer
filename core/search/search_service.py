"""
RO Database Explorer
Search Service

SQLiteから検索する処理を管理します。
"""

from core.database.connection import connect


def search_items(keyword: str):
    """
    アイテム名で検索
    """

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name
        FROM items
        WHERE name LIKE ?
        ORDER BY id
    """, (f"%{keyword}%",))

    result = cursor.fetchall()

    conn.close()

    return result