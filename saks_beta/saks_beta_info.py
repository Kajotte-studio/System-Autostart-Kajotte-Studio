"""
SAKS - System-Autostart-Kajotte-Studio
Version: Beta (v0.0.2)
Author: Kajotte Studio (kajotte-studio.com)
License: GNU General Public License v3.0

Status: Prace nad wersją BETA rozpoczęte / BETA version development started.
"""

import sys


def get_interface_data():
    """Zbiór komunikatów interfejsu w dwóch językach."""
    return {
        "pl": {
            "header": "SAKS - SYSTEM AUTOSTART KAJOTTE STUDIO",
            "status": "STATUS: ROZPOCZĘTO PRACE NAD WERSJĄ BETA",
            "license": "Licencja: GPLv3",
            "author": "Autor: Kajotte Studio (kajotte-studio.com)",
            "exit": "Naciśnij Enter, aby zamknąć..."
        },
        "en": {
            "header": "SAKS - SYSTEM AUTOSTART KAJOTTE STUDIO",
            "status": "STATUS: BETA VERSION DEVELOPMENT STARTED",
            "license": "License: GPLv3",
            "author": "Author: Kajotte Studio (kajotte-studio.com)",
            "exit": "Press Enter to close..."
        }
    }


def main():
    data = get_interface_data()
    
    print("1. English / 2. Polski")
    choice = input("Select / Wybierz (1/2): ").strip()
    
    lang = "en" if choice == "1" else "pl"
    ui = data[lang]
    
    print("\n" + "="*60)
    print(f"{ui['header']}")
    print(f"{ui['status']}")
    print("-" * 60)
    print(f"{ui['author']}")
    print(f"{ui['license']}")
    print("="*60)
    
    input(f"\n{ui['exit']}")


if __name__ == "__main__":
    main()