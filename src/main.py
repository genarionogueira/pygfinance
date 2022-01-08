import numpy as np
from scipy import interpolate

from typing import List
import datetime
from datetime import date

class LinearInterpolation(interpolate.interp1d):
    def __init__(self, x, y, kind='linear', axis=-1, copy=True, bounds_error=None, fill_value=..., assume_sorted=False):
        super().__init__(x, y, kind='linear', axis=axis, copy=copy, bounds_error=bounds_error, fill_value=fill_value, assume_sorted=assume_sorted)

class Curve:
    def __init__(self, 
                name:str, 
                points:List[float],
                dates:List[date],
                interp:interpolate.interp1d) -> None:
        pass
    def interpol(self,dt1,dt2)->float:
        pass

class BasicCurve(Curve):
    def __init__(self, name: str, points: List[float], dates: List[date]) -> None:
        super().__init__(name, points, dates)

