import aiosqlite

async def is_blacklisted(user_id):
    async with aiosqlite.connect("data/database.db") as db:
        async with db.execute("SELECT user_id FROM blacklist WHERE user_id=?", (str(user_id),)) as cur:
            return await cur.fetchone() is not None

async def is_owner(user_id):
    async with aiosqlite.connect("data/database.db") as db:
        async with db.execute("SELECT user_id FROM owners WHERE user_id=?", (str(user_id),)) as cur:
            return await cur.fetchone() is not None
