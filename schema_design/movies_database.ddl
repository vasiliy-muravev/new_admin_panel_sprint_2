CREATE SCHEMA IF NOT EXISTS content;

ALTER ROLE app SET search_path TO content,public;

CREATE TABLE IF NOT EXISTS content.film_work
(
    id            uuid PRIMARY KEY,
    title         TEXT NOT NULL,
    description   TEXT,
    creation_date DATE,
    file_path     TEXT,
    rating        FLOAT,
    type          TEXT not null,
    created_at    timestamp with time zone,
    updated_at    timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre
(
    id          uuid PRIMARY KEY,
    name        TEXT NOT NULL,
    description TEXT,
    created_at  timestamp with time zone,
    updated_at  timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work
(
    id           uuid PRIMARY KEY,
    genre_id     uuid    NOT NULL REFERENCES content.genre (id) ON DELETE CASCADE,
    film_work_id uuid    NOT NULL REFERENCES content.film_work (id) ON DELETE CASCADE,
    created_at   timestamp with time zone
);

CREATE UNIQUE INDEX film_work_genre ON genre_film_work (film_work_id, genre_id);

CREATE TABLE IF NOT EXISTS content.person
(
    id         uuid PRIMARY KEY,
    full_name  TEXT NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work
(
    id           uuid PRIMARY KEY,
    person_id    uuid    NOT NULL REFERENCES content.person (id) ON DELETE CASCADE,
    film_work_id uuid    NOT NULL REFERENCES content.film_work (id) ON DELETE CASCADE,
    role         TEXT    NOT NULL,
    created_at   timestamp with time zone
);

CREATE UNIQUE INDEX film_work_person_idx ON content.person_film_work (film_work_id, person_id, role);
