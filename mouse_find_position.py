import pyautogui

def show_mouse_position():
    try:
        while True:
            # Get the current mouse position
            x, y = pyautogui.position()

            # Print the mouse position in the terminal
            print(f"Mouse position: X={x}, Y={y}", end="\r", flush=True)
    except KeyboardInterrupt:
        print("\nScript terminated.")

if __name__ == "__main__":
    print("Press Ctrl+C to stop the script.")
    show_mouse_position()
