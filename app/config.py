from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    GROQ_API_KEY: str

    LLM_MODEL: str = "llama-3.1-8b-instant"
    VECTOR_DB_PATH: str = "vector_db"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    class Config:
        env_file = ".env"


settings = Settings()
