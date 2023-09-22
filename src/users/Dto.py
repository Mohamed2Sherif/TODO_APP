from dataclasses import dataclass, field
from datetime import date

@dataclass(frozen=True)
class User:
    username : str
    email : str
    first_name : str
    last_name : str
    password :str
    group:str
    created: date = field(default_factory=date.today)
    updated: date = field(default_factory=date.today)