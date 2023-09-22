from dataclasses import dataclass,field
from datetime import date

@dataclass(frozen=True)
class Task :
    title :str
    details : str
    deadline :date
    user : int
