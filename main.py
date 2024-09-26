from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Import By for new find_element syntax
import time

# Path to chrome driver
chrome_driver_path = r'C:\Users\baile\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Function to play the game
def play_game():
    # Open the 2048 game website
    driver.get("https://play2048.co/")

    # Find the game container (this is where the game listens for key events)
    game_container = driver.find_element(By.TAG_NAME, 'body')
    moves = [Keys.UP, Keys.LEFT, Keys.DOWN, Keys.RIGHT]
    #Can slow down or speed up, I wonder how fast I can make this
    delay = 0.001
    while True:
        for move in moves:
            game_container.send_keys(move)
            time.sleep(delay)

        # Check if the game is over (by looking for the "game-over" class)
        try:
            game_over_element = driver.find_element(By.CLASS_NAME, "game-over")
            print("Game over!")
            break
        except:
            # No game-over element found, continue playing
            continue

# Main loop to play the game multiple times
while True:
    play_game()
    print("Refreshing the page to start a new game...")
    driver.refresh()
    #delay before going through to ley mashing
    time.sleep(2) 
