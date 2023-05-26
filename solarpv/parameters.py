from dataclasses import dataclass
from typing import Optional


@dataclass
class Technical:
    lat: float
    lon: float
    capacity: float
    tilt: int
    azim: int
    dataset: Optional[str] = "merra2"
    date_from: Optional[str] = "2019-01-01"
    date_to: Optional[str] = "2019-12-31"
    system_loss: Optional[float] = 0.1
    tracking: Optional[float] = 0.0
    format: Optional[str] = "json"


@dataclass
class Financial:
    fit: float
    rate: Optional[float] = 0.05
    years: Optional[int] = 20
    invest: Optional[float] = 0.0
    other_expenses: Optional[float] = 0.0
