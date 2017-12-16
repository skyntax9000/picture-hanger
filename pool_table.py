import sys
import json
import datetime



class Table(object):
    def __init__ (self, number):
        self.number = number
        self.occupied = False

class Play(object):
    def __init__ (self, current_table):
    #    self.start_time = start_time
        self.current_table = current_table #this should just be the tables[i]
        #self.end_time = end_time
        #self.play_time = play_time
        #self.play_charge = play_charge

tables = []

for index in range(13):
    table = Table(index + 1)
    tables.append(table)

#tables = [for i in range(12): Table(i+1)]

print("Welcome to UH Pool Hall. Use this app to monitor the status of the pool tables.")

def menu():
    while True:
        menu_selection = str(raw_input("1: view current status of all 12 tables | 2: begin table play | 3: end table play | 4: send report | q: quit "))

        if menu_selection == "1":
            view_status()

        elif menu_selection == "2":
            begin_table_play()

        elif menu_selection == "3":
            end_table_play()

        elif menu_selection == "4":
            send_report()

        elif menu_selection == "q":
            quit()

        else:
         print("Invalid selection")
         menu()


def view_status():
    for tables[index] in tables:
        if tables[index].occupied == False:
            print ("{0}: Unoccupied").format(tables[index].number)
        else:
            print ("{0}: Occupied").format(tables[index].number)

#def no_more_available_tables():


def begin_table_play():
    for tables[index] in tables:
        if tables[index].occupied == False:
            tables[index].occupied = True
            table_play = Play(tables[index].number)
            return tables

def end_table_play():
    table_to_end_play = raw_input("Which table to end?")
    if table_to_end_play
def quit():
    sys.exit()

menu()
