from datetime import datetime

# Constants
MAX_ENTRIES = 5
FILENAME = "Patrick.txt"

# Function to write to both terminal and file
def log_output(text, file):
    print(text)
    file.write(text + "\n")

# Function to get user's name
def get_username():
    name = input("What is your name?\n> ").strip()
    return name

# Function to get and validate a date
def get_valid_date():
    while True:
        date_input = input("Date (dd/mm/yyyy): ").strip()
        try:
            datetime.strptime(date_input, "%d/%m/%Y")
            return date_input
        except ValueError:
            print("❌ Invalid date format. Please use dd/mm/yyyy")

# Function to get and validate mood rating
def get_mood_rating(file):
    while True:
        mood_input = input("Rate your mood (1-10): ").strip()
        try:
            mood = int(mood_input)
            if 1 <= mood <= 10:
                # Mood feedback
                if mood >= 8:
                    log_output("😊 Glad you're feeling great!", file)
                elif mood >= 5:
                    log_output("🙂 Hope tomorrow's even better!", file)
                else:
                    log_output("😟 Hang in there. Better days are ahead.", file)
                return mood
            else:
                log_output("⚠️ Please enter a number between 1 and 10", file)
        except ValueError:
            log_output("⚠️ Invalid input. Please enter a number.", file)

# Function to get diary entry
def get_entry():
    entry = input("Write your diary entry:\n> ").strip()
    return entry

# Function to display all entries
def display_entries(dates, moods, entries, word_counts, file):
    log_output("\n" + "="*20 + " ALL ENTRIES " + "="*20, file)
    for i in range(len(dates)):
        log_output(f"\nEntry {i + 1} - {dates[i]}", file)
        log_output(f"Mood: {moods[i]}/10", file)
        log_output(f"Entry:\n{entries[i]}", file)
        log_output(f"Word Count: {word_counts[i]}", file)

# Function to display summary
def display_summary(moods, dates, entries, word_counts, file):
    average_mood = sum(moods) / len(moods)
    log_output(f"\n📊 Average Mood: {average_mood:.2f}/10", file)

    # Longest entry
    max_words = max(word_counts)
    index = word_counts.index(max_words)
    log_output("\n" + "="*20 + " LONGEST ENTRY " + "="*20, file)
    log_output(f"Date: {dates[index]}", file)
    log_output(f"Word Count: {word_counts[index]}", file)
    log_output(f"{entries[index]}", file)

# Main diary loop
def main():
    name = get_username()
    
    # Open file for writing (overwrite if exists)
    with open(FILENAME, "w", encoding="utf-8") as file:
        log_output(f"\nHello, {name}!\n", file)

        date_str = []
        mood_num = []
        entries = []
        word_counts = []

        for i in range(MAX_ENTRIES):
            log_output("="*50 + f"\nWelcome to your Diary, {name}!!\n" + "="*50, file)

            date = get_valid_date()
            mood = get_mood_rating(file)
            entry = get_entry()

            date_str.append(date)
            mood_num.append(mood)
            entries.append(entry)
            word_counts.append(len(entry.split()))

        display_entries(date_str, mood_num, entries, word_counts, file)
        display_summary(mood_num, date_str, entries, word_counts, file)

# Run the program
if __name__ == "__main__":
    main()
