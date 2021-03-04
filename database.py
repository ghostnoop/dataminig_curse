from abc import ABC

import asyncpg


class ConfigurableDB(ABC):
    pool: asyncpg.pool.Pool

    @classmethod
    def configurate(cls, pool: asyncpg.pool.Pool):
        cls.pool = pool


class TopWords(ConfigurableDB):
    CREATE_TABLE = (
        "CREATE TABLE IF NOT EXISTS top_words "
        "( "
        "id SERIAL PRIMARY KEY "
        "text VARCHAR(256),"
        "result_of INTEGER "
        "); "
    )

    @classmethod
    async def create_table(cls):
        await cls.pool.execute(cls.CREATE_TABLE)




async def preapare_db(*args, **kwargs):
    pool = await asyncpg.create_pool(user="marat", password="postgres",
                                     database="datamining", host="localhost")

    TopWords.configurate(pool)
    await TopWords.create_table()
