import math

# FIRST EXAMPLE
# print("Hellow world")
# print('Hellow, how are you doing?')
# diary_entry_date = '25/05/2025'
# Mood_level = 8
# sleep_hour = 7.5
# is_favorite = True
# print(f'Date: {Mood_level/10}')
# print(f'SleepHour: {sleep_hour}hours')
# print(f'Favorite: {is_favorite}')
# entry_text = 'Had an Amazing day learning Python!'
# print(type(entry_text))

# # EXAMPLE USER INPUT
# print('Welcome To Smart Dairy?')
# name = input("What is your name? ")
# date = input("What's today's date? ")
# mood = input("Rate your mood (1-10); ")
# entry = input("Tell me about your day:")
# print("\n"+"="*40)
# print(f'Date: {date}')
# print(f'Author: {name}')
# print(f'Mood: {mood}')
# print(f'Entry: {entry}')
# print("="*40)
# print(f'Entry Saved')
#
# #converting user input for string
# mood_str = input('Rate your mood (1-10):')
# mood_num= int(mood_str)
# print(f'Your mood level: {mood_num}')
# #calculate average mood over time
# total_mood = mood_num +7+9
# #previus entries
# average = total_mood /3
# print(f'Average mood: {average:.1f}')
# print(type(average))

# #Example ON String method
# data_input = '25/05/2025'
# day = data_input[0:2]#"25"
# month = data_input[3:5]#"05"
# year = data_input[6:10]#"2025"
# print(f'Day: {day}, Month: {month}, Year: {year}')
# #previus entries
# entry = "Today was an Amazing Day! I have learn Python!"
# clean_entry = entry.strip().lower()
# words = clean_entry.split()
# word_count = len(words)
# print(f'Word Count: {word_count}')
# print(f'Words: {words}')
# #finding rewords
# if'python' in clean_entry:
#     print('You mentioned Python!')

#Diary Application
#name = input("Enter your name: ")
# def personalized_greeting(name):
#     print(f'Hello, {name} Welcome to your Diary!') #Display a personal greeting
# def collect_diary_entries(number_of_entries):
#   entries = [] #Collect diary entries from the users
#   for i in range(number_of_entries):
#       entry = int(input(f'Enter a number{i+1}: '))
#       entries.append(entry) #add entry
#   return entries
# def calculate_average_mood(entries): # Calculate the average mood based on user's rating
#   total_mood = 0
#   for i in range(len(entries)):
#       mood = input(f'Rating your mood for entry{i+1}(1-10): ')
#       total_mood += mood
#   return total_mood / len(entries)
# def find_longest_entry(entries): #Find the longest diary entry
#     longest_entry = max(entries, key=len)
#     return longest_entry
# def word_count(entries): #count words in each entry
#     counts = [len(entry.split()) for entry in entries]
#     return counts
# def display_entries(entries): #Disply all Diary entries
#     print("\n Your Diary Entries:")
#     for i, entry in enumerate(entries):
#         print(f'Entry {i+1}: {entry}')
# def main():
#     #personalized greeting
#     name = input("Enter your name: ")
#     personalized_greeting(name)
#     #collect diary entry
#     number_of_entries = input("Enter number of entries: ")
#     entries = collect_diary_entries(number_of_entries)
#     #display
#     display_entries(entries)
#     #calculate and show average mood
#     average_mood = calculate_average_mood(entries)
#     print(f"\n Your average mood: {average_mood:.2f}")
#     #Find and display the longest entry
#     longest_entry = find_longest_entry(entries)
#     print(f"\n Your longest entry: {longest_entry}")
#     #Word count for each entry
#     counts = word_count(entries)
#     for i, count in enumerate(counts):
#         print(f'Entry {i+1} Word count: {count}')
#
# if __name__ == '__main__':
#     main()

# Diary Entry Collector
# print("Create Your Diary Entry")
# print("-"*30)
# #Collect information
# date = input("Enter today's Date : ")
# mood = input("Rate your mood : ")
# text = input("Write your entry : ")
# # covert mood to integer
# mood_number = int(mood)
# diary_entry = [mood_number, text]
# diary_entry.append(date)
# print(diary_entry)
# print("+""="*40)
# print("Entry is saved successfully!")
# print("="*40)
#
# #date parser
# date = "26/05/2025"
# day = date[0:2] #26
# month = date[4:5] #05
# year = date[6:10]  #2026
# print(f'Day: {day}')
# print(f'Month: {month}')
# print(f'Year: {year}')
#
# # Text Analyzer
# diary_entry = 'Today Was An Amazing Day For Me, I Learn Alot On Python Programing'
# clean_entry = diary_entry.strip().lower()
# words = clean_entry.split()
# word_count = len(words)
# print(words)
# print(f'Word Count: {word_count}')
#
# #finding rewords
# n = input("Enter the value of n: ")
# if n in clean_entry:
#     print('You mentioned Python!')


#Assignment one
user_name = input("Enter your name: ")
print(f'Hello {user_name}! You ar most welcome to our Diary Farm') #Display a personal greeting

#informationof from users
place = input('Where do you live? ')
date = input("What's today's date? ")
mood = input("Rate your mood (1-10): ")
entry = input("Tell me about your day: ")
quantity = input('how many litter of milk do you want: ')
#Display
print("\n"+"="*50)
print(f'Date: {date}')
print(f'Mood: {mood}')
print(f'Entry: {entry}')
print(f'Quantity: {quantity}')
print("="*50)
print(f'Entry Saved')

#converting user input for string
mood_str = input('Rate your mood (1-10):')
mood_num= int(mood_str)
print(f'Your mood level: {mood_num}')

#calculate average mood over time
total_mood = mood_num +7+9+5+6

#previus entries
average = total_mood /5
print(f'The Average mood is: {average:.2f}')

#To find and Display the longest entry
diary_entries = [] #An empty list
entry1 = 'Today I started with introduction to Python'
entry2 = 'Python is so interesting right from the introduction'
entry3 = 'I looked at most the datatype and variables'
entry4 = 'I wasc able to complete some exercise and an assignment'
entry5 = 'I also built my first project'
# Add entries to the list created
diary_entries.append(entry1)
diary_entries.append(entry2)
diary_entries.append(entry3)
diary_entries.append(entry4)
diary_entries.append(entry5)
print(f'Total entries: {len(diary_entries)}')

#Find and display the longest entry
longest_entry = max(diary_entries, key=len)
print(f"\n Your longest entry: {longest_entry}")

#calculate word count for each entry
for i, entry in enumerate(diary_entries, start=1):
    word_cont = len(entry.split())
    print(f"\nEntry {i}: {entry} | Word Count: {word_cont}")

