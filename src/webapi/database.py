from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import settings

# создание движка
engine = create_engine(
    settings.database_url, # расположение базы данных
    connect_args={'check_same_thread': False} # работать только в одном потоке
)

# созжание сессии
Session = sessionmaker(
    engine,
    autoflush=False, # отключается авто выгрузка и подтверждение
    autocommit=False
)


def get_session()->Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()