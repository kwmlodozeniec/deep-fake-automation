import time

import obsws_python as obs
import pyautogui as pag
from pyautogui import Point

from constants import ManyCamHotKeys, ManyCamPoints, SwapfaceHotKeys, SwapfacePoints

OBS_CLIENT = obs.ReqClient(host="localhost", port=4455, password="", timeout=3)


def get_screen_size():
    return pag.size()


def to_screen_center():
    screen_size = get_screen_size()
    pag.moveTo(screen_size.width // 2, screen_size.height // 2)


def go_to_point_from_center(point: Point):
    to_screen_center()
    pag.moveRel(point.x, point.y)


def setup_manycam(img_idx: int):
    print(f"Setting up ManyCam with image {img_idx+1}...")
    pag.PAUSE = 1  # This delay seems sufficient between actions in ManyCam
    pag.hotkey(*ManyCamHotKeys.activate)

    to_screen_center()
    pag.hotkey(*ManyCamHotKeys.clear_scene)
    pag.click()
    pag.moveRel(ManyCamPoints.add_image)
    pag.click()
    go_to_point_from_center(ManyCamPoints.img_positions[img_idx])
    pag.click()
    go_to_point_from_center(ManyCamPoints.open_image)
    pag.click()
    to_screen_center()


def setup_swapface(img_idx: int):
    print(f"Setting up SwapFace with image {img_idx+1}...")
    pag.PAUSE = 3  # Swapface is very slow to respond to user input
    pag.hotkey(*SwapfaceHotKeys.activate)
    go_to_point_from_center(SwapfacePoints.add_more_positions[img_idx])
    pag.click()
    go_to_point_from_center(SwapfacePoints.img_positions[img_idx])
    pag.click()
    go_to_point_from_center(SwapfacePoints.start)
    pag.click()
    time.sleep(5)  # short delay as swapface can be a bit slow to start


def stop_swapface():
    print("Stopping SwapFace...")
    go_to_point_from_center(SwapfacePoints.start)
    pag.click()
    time.sleep(5)  # short delay as swapface can be a bit slow to start


if __name__ == "__main__":
    for img_idx in range(5):
        setup_manycam(img_idx)
        setup_swapface(img_idx)
        print("Starting recording...")
        OBS_CLIENT.start_record()
        time.sleep(5)
        print("Stopping recording...")
        recording = OBS_CLIENT.stop_record()
        stop_swapface()
        print(recording.output_path)
