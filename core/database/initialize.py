"""
RO Database Explorer

Database Initializer

Author : ALTRISE
Edition : Public / Rainbow
Database : SQLite

Purpose
-------
SQLiteデータベースの初期化を担当する。
テーブル作成・初期化処理をここで管理する。
"""

from .connection import connect, DATABASE_PATH
from .connection import connect


def initialize_database():
    print("Database Path:", DATABASE_PATH)
    """SQLiteデータベースを初期化する"""

    conn = connect()
    print("Database Connected!")
    cursor = conn.cursor()

    # =====================================================
    # Items
    # =====================================================
    # ROアイテム情報
    #
    # 今後追加予定
    # - type
    # - description
    # - atk
    # - matk
    # - def
    # - slots
    # - weight
    # =====================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    """)

    cursor.executemany("""
    INSERT OR IGNORE INTO items (id, name)
    VALUES (?, ?)
    """, [
        (1001, "ポリン"),
        (1002, "ルナティック"),
        (1003, "ポポリン"),
        (1004, "マーリン"),
    ])

    # =====================================================
    # Future Tables
    # =====================================================
    # monsters
    # cards
    # maps
    # npc
    # quests
    # skills
    # achievements
    # enchantments
    # build_presets (Rainbow Edition)
    # advisor_cache (Rainbow Edition)
    # =====================================================

    conn.commit()
    conn.close()