import aiosqlite

DB_PATH = "data/database.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS prefixes (guild_id TEXT, prefix TEXT)")
        await db.execute("CREATE TABLE IF NOT EXISTS blacklist (user_id TEXT)")
        await db.execute("CREATE TABLE IF NOT EXISTS owners (user_id TEXT)")
        await db.commit()
