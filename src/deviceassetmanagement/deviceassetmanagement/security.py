from pydantic import field_validator

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Security(BaseSettings):
    allowed_hosts: list[str]
    secret_key: str
    debug: bool
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="DJANGO_",
        env_file_encoding="utf-8",
    )
    
    
    @field_validator("allowed_hosts")
    @classmethod
    def clean_hosts(cls, v):
        return [host.strip() for host in v if host.strip()]


    
    

security = Security()