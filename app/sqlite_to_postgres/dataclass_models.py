import datetime

from dataclasses import dataclass
from uuid import uuid4

# Объект фильма через dataclass
@dataclass
class FilmWork:
    id: uuid4
    title: str
    description: str
    creation_date: datetime or None
    file_path: str or None
    rating: float
    type: str
    created_at: datetime
    updated_at: datetime


# Объект персоны через dataclass
@dataclass
class Person:
    id: uuid4
    full_name: str
    created_at: datetime
    updated_at: datetime


# Объект жанра через dataclass
@dataclass
class Genre:
    id: uuid4
    name: str
    description: str or None
    created_at: datetime
    updated_at: datetime


# Объект связи через dataclass
@dataclass
class GenreFilmWork:
    id: uuid4
    genre_id: uuid4
    film_work_id: uuid4
    created_at: datetime


# Объект связи через dataclass
@dataclass
class PersonFilmWork:
    id: uuid4
    person_id: uuid4
    film_work_id: uuid4
    role: str
    created_at: datetime