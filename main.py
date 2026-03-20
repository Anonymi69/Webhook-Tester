import requests
import os
import sys
import time
import threading
from colorama import init, Fore, Style

init(autoreset=True)

ASCII_ART = [
    " ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ████████╗███████╗███████╗████████╗███████╗██████╗ ",
    " ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗",
    " ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝        ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝",
    " ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗        ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗",
    " ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗       ██║   ███████╗███████║   ██║   ███████╗██║  ██║",
    "  ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝       ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝",
]

ASCII_GRADIENT = [
    (255,   0, 0),
    (255,  60, 0),
    (255, 120, 0),
    (255, 180, 0),
    (255, 220, 0),
    (255, 255, 0),
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_ascii():
    import shutil
    clear_screen()
    term_w = shutil.get_terminal_size().columns
    max_w  = max(len(line) for line in ASCII_ART)
    pad    = max((term_w - max_w) // 2, 0)
    indent = ' ' * pad
    print()
    for i, line in enumerate(ASCII_ART):
        r, g, b = ASCII_GRADIENT[i]
        print(f"\033[38;2;{r};{g};{b}m{indent}{line}\033[0m")
    print()
    import shutil as sh
    tw = sh.get_terminal_size().columns
    credit = "~ Made By GHO5T ~"
    ORANGE = "\033[38;2;255;140;0m"
    print(Fore.GREEN + credit.center(tw))
    print()


def animated_dots(prefix, duration=2.0):
    frames = ["   ", ".  ", ".. ", "..."]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{Fore.MAGENTA}{prefix}{frames[i % len(frames)]}", end="", flush=True)
        time.sleep(0.25)
        i += 1
    print(f"\r{Fore.MAGENTA}{prefix}...   ", flush=True)


def animated_enter_prompt():
    msg = "  Press Enter To Exit"
    frames = ["   ", ".  ", ".. ", "..."]
    stop_event = threading.Event()

    def animate():
        i = 0
        while not stop_event.is_set():
            print(f"\r{Fore.MAGENTA}{msg}{frames[i % len(frames)]}", end="", flush=True)
            time.sleep(0.35)
            i += 1

    t = threading.Thread(target=animate, daemon=True)
    t.start()
    input()
    stop_event.set()
    t.join()


def main():
    print_ascii()
    time.sleep(2)

    webhook_url = input(Fore.CYAN + "  Enter your Discord webhook URL: ").strip()

    if not webhook_url:
        animated_dots("  No webhook URL provided! Exiting", duration=2.0)
        sys.exit(0)

    message = "✅ Test message from Webhook Tester"

    animated_dots("  Validating", duration=4.0)

    data = {"content": message}

    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code in (200, 204):
            print(Fore.GREEN + "\n  Webhook test succeeded! ")
        else:
            print(Fore.RED + f"\n  Webhook test failed. Status code: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"\n  Error: {e}")

    animated_enter_prompt()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        animated_dots("  Exiting", duration=2.0)
