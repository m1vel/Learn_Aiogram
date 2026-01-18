from dataclasses import dataclass

@dataclass
class DB_Config:
    host: str
    user: str
    password: str
    database: str

@dataclass
class Bot:
    token: str
    admin_ids: list[str]
  
@dataclass
class Config:
    bot: Bot
    db: DB_Config
