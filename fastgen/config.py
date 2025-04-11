from pydantic import BaseModel
from typing import Optional
import toml

class FastGenConfig(BaseModel):
    project_name: str
    with_auth: bool = False
    with_docker: bool = False
    db: Optional[str] = None  # postgres, sqlite, etc.

    @classmethod
    def from_file(cls, path: str):
        config_data = toml.load(path)
        return cls(**config_data)