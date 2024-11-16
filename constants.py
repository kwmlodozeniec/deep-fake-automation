from dataclasses import dataclass

from pyautogui import Point


@dataclass(frozen=True)
class ManyCamHotKeys:
    activate: tuple[str, ...] = ("alt", "ctrl", "m")
    clear_scene: tuple[str, ...] = ("shift", "backspace")
    center_file_picker: tuple[str, ...] = ("win", "alt", "ctrl", "shift", "c")


@dataclass(frozen=True)
class ManyCamPoints:
    add_image: Point = Point(x=50, y=210)
    img_positions: tuple[Point, ...] = (
        Point(x=220, y=-290),
        Point(x=220, y=-270),
        Point(x=220, y=-250),
        Point(x=220, y=-230),
        Point(x=220, y=-210),
    )
    open_image: Point = Point(x=340, y=50)


@dataclass(frozen=True)
class SwapfaceHotKeys:
    activate: tuple[str, ...] = ("alt", "ctrl", "s")


@dataclass(frozen=True)
class SwapfacePoints:
    add_more_positions: tuple[Point, ...] = (
        Point(x=-766, y=320),
        Point(x=-555, y=324),
        Point(x=-358, y=327),
        Point(x=-155, y=324),
        Point(x=50, y=299),
    )
    img_positions: tuple[Point, ...] = (
        Point(x=-357, y=-137),
        Point(x=-216, y=-131),
        Point(x=-76, y=-129),
        Point(x=58, y=-124),
        Point(x=197, y=-129),
    )
    start: Point = Point(x=709, y=196)
