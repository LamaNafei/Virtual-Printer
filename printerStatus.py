from enum import Enum


class PrinterStatus(Enum):
    Idle = 1
    Printing = 2
    PaperJam = 3
    OutOfPaper = 4
    Offline = 5
    LowInkOrToner = 6
    Error = 7
    Busy = 8
    Paused = 9
    Cancelled = 10
    Unknown = 11