"""
Today I Learned (TIL) Journal

Purpose:
This simple Python program helps you keep track of what you learn every day.
You can add a new note for today or view all your past notes, which are saved
locally in a file called 'entries.json'. It’s a neat little way to build a daily
learning habit and look back on your progress over time.
"""

import json      # To save and load your journal entries
import os        # To check if your entries file exists
from datetime import date  # To get today’s date

# This is the file where we'll keep all your TIL notes
FILENAME = "entries.json"

def load_entries():
    # If the file with your notes exists, open and read it
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)  # Load your saved notes as a dictionary
    else:
        # If there’s no file yet, just start fresh with an empty dictionary
        return {}

def save_entries(entries):
    # Save your notes back to the file, nicely formatted
    with open(FILENAME, "w") as file:
        json.dump(entries, file, indent=4)

def add_entry():
    today = str(date.today())  # Get today’s date as a string, like "2025-08-29"
    entries = load_entries()   # Load existing notes

    # Check if you’ve already written something today
    if today in entries:
        print(f"\nLooks like you've already added something for today ({today}):")
        print(f"\"{entries[today]}\"")
        return  # Don’t add a second note for the same day

    print("\nWhat did you learn today?")
    entry = input(">>> ").strip()  # Get your input and clean up spaces

    if entry:
        entries[today] = entry  # Save your note for today
        save_entries(entries)   # Write it to the file
        print(f"\nAwesome! Your entry for {today} has been saved ✅")
    else:
        print("Oops! You didn’t write anything, so nothing was saved.")

def view_entries():
    entries = load_entries()  # Grab all your saved notes

    if not entries:
        print("\nYou haven’t written anything yet. Why not add your first TIL?")
        return

    print("\nHere’s everything you’ve learned so far:")
    # Show the newest notes first
    for day in sorted(entries.keys(), reverse=True):
        print(f"{day}: {entries[day]}")

def main():
    print("\n👋 Welcome to your Today I Learned Journal!")
    print("What would you like to do?")
    print("1. Add a new entry")
    print("2. See all your entries")

    choice = input("\nType 1 or 2: ").strip()

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    else:
        print("Hmm, that’s not a valid choice. Please try again!")

if __name__ == "__main__":
    main()
