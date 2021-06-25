# Application information, data and enums
from enum import Enum

Version = "1.0.1"
Stable = "Alfa"
SVer = "001"
Credits = "@FunkyoEnma 2021"


class Args(Enum):

    InputImage = 1
    EnableRounded = 2


class ImageTypes(Enum):

    Squared = 1
    Rounded = 2
    Portrait = 3
    Landscape = 4


avaibleArgs = {Args.InputImage: ["input", "image", "original", "i", "ii", "oi", "inputimage"]}
validFormats = ["jpg", "png"]
defaultArgs = {Args.EnableRounded: False}
