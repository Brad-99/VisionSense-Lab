# from pynput import keyboard
# import pyautogui
# import utils
# import handler
#
#
# def loadImageClick(title):
#     REQUIRED_POS = 2
#     positions = []
#
#     def on_release(key):
#         if key == keyboard.Key.ctrl_l:  # Press left ctrl
#             mousePos = pyautogui.position()
#             positions.append(utils.Point(mousePos.x, mousePos.y))
#             if len(positions) == REQUIRED_POS:
#                 return False
#
#     # The event listener will be running in this block
#     with keyboard.Listener(on_release=on_release) as listener:
#         listener.join()
#
#     utils.loadImageWindow(title, loadImageClick, submitImageClick, positions)

#def submitImageClick(pos):
#    handler.updateLoadedImageToScreen(pos)

#JEFFS CODE
# from pynput import keyboard
# import pyautogui
# import utils
# import handler
# import cv2
# import win32gui
# import mss
# import time
# import numpy as np
#
#
# class ScreenHandler:
#     MINIMAP_BOTTOM_BORDER = 9
#     MINIMAP_TOP_BORDER = 5
#     MM_TL_TEMPLATE = cv2.imread('pics/minimap_tl_template.png', 0)
#     MM_BR_TEMPLATE = cv2.imread('pics/minimap_bl_template.png', 0)
#     MMT_HEIGHT = max(MM_TL_TEMPLATE.shape[0], MM_BR_TEMPLATE.shape[0])
#     MMT_WIDTH = max(MM_TL_TEMPLATE.shape[1], MM_BR_TEMPLATE.shape[1])
#
#     PLAYER_TEMPLATE = cv2.imread('pics\\playerIcon.png', 0)
#     PT_HEIGHT, PT_WIDTH = PLAYER_TEMPLATE.shape
#
#     OTHER_PLAYER_TEMPLATE = cv2.imread('pics\\redIcon.png', 0)
#     OPT_HEIGHT, OPT_WIDTH = OTHER_PLAYER_TEMPLATE.shape
#
#     RUNE_TEMPLATE = cv2.imread('pics\\runeIcon.png', 0)
#     RT_HEIGHT, RT_WIDTH = RUNE_TEMPLATE.shape
#
#     def screenshot(self, region=None):
#         with mss.mss() as sct:
#             sct.compression_level = 0  # For faster transfers (optional).
#
#             if region:
#                 sct_img = sct.grab(region)
#                 return np.array(sct_img)
#             else:
#                 sct_img = sct.shot(output=None)
#                 return cv2.imread(sct_img)
#
#     def improved_single_match(self, frame, template):
#         # Apply template Matching with masking (if you have a mask available)
#         method = cv2.TM_CCOEFF_NORMED
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         res = cv2.matchTemplate(gray, template, method)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#
#         # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#         if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#             top_left = min_loc
#         else:
#             top_left = max_loc
#
#         # Use a stricter threshold to determine a match
#         threshold = 0.8  # for example
#         if max_val < threshold:
#             return None  # No match found with the required certainty
#
#         bottom_right = (top_left[0] + w, top_left[1] + h)
#         return top_left, bottom_right
#
#     def single_match(self, frame, template):
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
#         _, _, _, top_left = cv2.minMaxLoc(result)
#         w, h = template.shape[::-1]
#         bottom_right = (top_left[0] + w, top_left[1] + h)
#         return top_left, bottom_right
#
#     def feature_based_matching(self, frame, template):
#         # Convert images to grayscale
#         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
#
#         # Detect ORB keypoints and descriptors in images
#         orb = cv2.ORB_create()
#         keypoints1, descriptors1 = orb.detectAndCompute(gray_frame, None)
#         keypoints2, descriptors2 = orb.detectAndCompute(gray_template, None)
#
#         # Create matcher with crossCheck turned on for better matching
#         bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#         matches = bf.match(descriptors1, descriptors2)
#
#         # Sort the matches based on their distance (the lower the better)
#         good_matches = sorted(matches, key=lambda x: x.distance)
#
#         # You might want to set a threshold or take the top N matches here
#         if len(good_matches) > N:  # N being a number based on your criteria
#             good_matches = good_matches[:N]
#
#         # Draw the matches (for visualization purposes)
#         result = cv2.drawMatches(frame, keypoints1, template, keypoints2, good_matches, None)
#
#         return result  # or any other information you need
#
#     def multi_match(self, frame, template, threshold=0.95):
#         if template.shape[0] > frame.shape[0] or template.shape[1] > frame.shape[1]:
#             return []
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
#         locations = np.where(result >= threshold)
#         locations = list(zip(*locations[::-1]))
#         results = []
#         for p in locations:
#             x = int(round(p[0] + template.shape[1] / 2))
#             y = int(round(p[1] + template.shape[0] / 2))
#             results.append((x, y))
#         return results
#
#     def get_player_position(self, game_window_rect):
#         rect = game_window_rect
#
#         width = max(rect[2] - rect[0], self.MMT_WIDTH)
#         height = max(rect[3] - rect[1], self.MMT_HEIGHT)
#
#         # Screenshot the whole game window
#         frame = self.screenshot(region={"top": rect[1], "left": rect[0], "width": width, "height": height})
#
#         # Calibrate by finding the top-left and bottom-right corners of the minimap
#         tl, _ = self.single_match(frame, self.MM_TL_TEMPLATE)
#         _, br = self.single_match(frame, self.MM_BR_TEMPLATE)
#
#         mm_tl = (tl[0] + self.MINIMAP_BOTTOM_BORDER, tl[1] + self.MINIMAP_TOP_BORDER)
#         mm_br = (
#             max(mm_tl[0] + self.PT_WIDTH, br[0] - self.MINIMAP_BOTTOM_BORDER),
#             max(mm_tl[1] + self.PT_HEIGHT, br[1] - self.MINIMAP_BOTTOM_BORDER)
#         )
#
#         # Crop the frame to only show the minimap
#         minimap = frame[mm_tl[1]:mm_br[1], mm_tl[0]:mm_br[0]]
#         player = self.multi_match(minimap, self.PLAYER_TEMPLATE, threshold=0.8)
#         # cv2.imshow('Minimap', minimap)
#         # if cv2.waitKey(1) == 27:  # ESC key pressed
#         #    return None
#         if player:
#             player_pos = player[0]
#             return player_pos
#         else:
#             return None
#
#     def locate_on_screen(self, confidence=0.99, grayscale=False, region=None):
#         """
#         Locate an image on the screen using template matching.
#
#         :param confidence: Matching confidence threshold.
#         :param grayscale: Whether to convert the images to grayscale for matching.
#         :param region: Tuple specifying the region (x, y, width, height) within which to search.
#         :return: A list of bounding boxes where the image was found.
#         """
#         # Hard-coded path to the image file
#         template_path = 'pics\\redIcon.png'
#         template = cv2.imread(template_path, 0 if grayscale else -1)
#
#         # Capture the screen
#         with mss.mss() as sct:
#             monitor = {"top": region[1], "left": region[0], "width": region[2], "height": region[3]} if region else \
#             sct.monitors[0]
#             screenshot = np.array(sct.grab(monitor))
#
#         # Convert screenshot to gray if necessary
#         if grayscale or len(template.shape) == 2:
#             screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
#
#         # Apply template matching
#         res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
#         locations = np.where(res >= confidence)
#
#         # Translate match results into bounding boxes
#         bounding_boxes = []
#         h, w = template.shape[:2]
#         for pt in zip(*locations[::-1]):  # Swap columns and rows
#             bounding_boxes.append((pt[0], pt[1], w, h))
#
#         return bounding_boxes
#
#     def check_other_player_presence(self, confidence=0.99, grayscale=False, region=None):
#         """
#         Check if the 'other player' image is present on the screen.
#
#         :param confidence: Matching confidence threshold.
#         :param grayscale: Whether to convert the images to grayscale for matching.
#         :param region: Tuple specifying the region (x, y, width, height) within which to search.
#         :return: Boolean indicating if the image is present.
#         """
#         found_locations = self.locate_on_screen(confidence=confidence, grayscale=grayscale, region=region)
#         return len(found_locations) > 0

#Jay's CODE

from pynput import keyboard
import pyautogui
import utils
import handler
import cv2
import win32gui
import mss
import time
import numpy as np

# Constants (Update these as per your existing setup)
MINIMAP_BOTTOM_BORDER = 5  # Placeholder values
MINIMAP_TOP_BORDER = 5
MM_TL_TEMPLATE = cv2.imread(r'C:\Users\rayra\Code\maple\ekko\ekko\pics\minimap_tl_template.png', 0)
MM_BR_TEMPLATE = cv2.imread(r'C:\Users\rayra\Code\maple\ekko\ekko\pics\minimap_br_template.png', 0)
MMT_HEIGHT = max(MM_TL_TEMPLATE.shape[0], MM_BR_TEMPLATE.shape[0])
MMT_WIDTH = max(MM_TL_TEMPLATE.shape[1], MM_BR_TEMPLATE.shape[1])

def get_game_window_rect():
    hwnd = win32gui.FindWindow(None, 'MapleStory')
    if not hwnd:
        return None
    return win32gui.GetWindowRect(hwnd)


def screenshot(region=None):
    with mss.mss() as sct:
        sct.compression_level = 0  # For faster transfers (optional).

        if region:
            sct_img = sct.grab(region)
            return np.array(sct_img)
        else:
            # Code for capturing the entire screen or specific monitor
            # Note: This code will take a screenshot of the primary monitor
            sct_img = sct.shot(output=None)
            return cv2.imread(sct_img)


def single_match(frame, template):
    """
    Finds the best match within FRAME.
    :param frame:       The image in which to search for TEMPLATE.
    :param template:    The template to match with.
    :return:            The top-left and bottom-right positions of the best match.
    """

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
    _, _, _, top_left = cv2.minMaxLoc(result)
    w, h = template.shape[::-1]
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left, bottom_right

def loadImageClick(title):
    REQUIRED_POS = 2
    positions = []

    def on_release(key):
        if key == keyboard.Key.ctrl_l:  # Press left ctrl
            rect = get_game_window_rect()
            width = max(rect[2] - rect[0], MMT_WIDTH)
            height = max(rect[3] - rect[1], MMT_HEIGHT)

            # Screenshot the whole game window
            frame = screenshot(region={"top": rect[1], "left": rect[0], "width": width, "height": height})

            # Calibrate by finding the top-left and bottom-right corners of the minimap
            tl, _ = single_match(frame, MM_TL_TEMPLATE)
            _, br = single_match(frame, MM_BR_TEMPLATE)

            # Get the window's position relative to its parent
            hwnd = win32gui.FindWindow(None, 'MapleStory')
            relative_x, relative_y, _, _ = win32gui.GetWindowRect(hwnd)

            # Calculate the absolute position by adding the parent's position (if it's a child window)
            relative_x, relative_y, _, _ = win32gui.GetWindowRect(hwnd)
            print(relative_x + tl[0], relative_y + tl[1])
            print(relative_x + br[0], relative_y + br[1])

            positions.append(utils.Point(relative_x + tl[0], relative_y + tl[1]))
            positions.append(utils.Point(relative_x + br[0], relative_y + br[1]))
            if len(positions) == REQUIRED_POS:
                return False

    # The event listener will be running in this block
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

    utils.loadImageWindow(title, loadImageClick, submitImageClick, positions)


def submitImageClick(pos):
    handler.updateLoadedImageToScreen(pos)

