import time
'''
--- Day 2: Red-Nosed Reports ---

Fortunately, the first location The Historians want to search isn't a long 
walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to 
contain no sign of the Chief Historian, the engineers there run up to you 
as soon as they see you. Apparently, they still talk about the time Rudolph 
was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really 
appreciate your help analyzing some unusual data from the Red-Nosed 
reactor. You turn to check if The Historians are waiting for you, but they 
seem to have already divided into groups that are currently searching every 
corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report 
per line. Each report is a list of numbers called levels that are separated 
by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-
Nosed reactor safety systems can only tolerate levels that are either 
gradually increasing or gradually decreasing. So, a report only counts as 
safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking 
those rules:

     - 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
     - 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
     - 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
     - 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
     - 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
     - 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

To begin, get your puzzle input (day_2_puzzle_input).
'''

def report_safety_check(report:list) -> bool:
    difference_check = [report[x+1] - report[x] for x in range(len(report)-1)]
    if (all(x < 0 and x in range(-3, 0) for x in difference_check) or 
        all(x > 0 and x in range(1,4) for x in difference_check)):
        return True
    else:
        return False

file = open('.\\day_2\\day_2_puzzle_input.txt')
raw_input = file.read().split('\n')
sanatized_input = []
for report in raw_input:
    temp_list_string = report.split()
    temp_list_int = [int(x) for x in temp_list_string]
    sanatized_input.append(temp_list_int)
    
safe_report_counter_1 = 0
for report in sanatized_input:      
    result = report_safety_check(report)
    if result == True:
        safe_report_counter_1 += 1
        
print('Number of safe reports: ', safe_report_counter_1)

'''
--- Part Two ---

The engineers are surprised by the low number of safe reports until they 
realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor 
safety systems tolerate a single bad level in what would otherwise be a 
safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from 
an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can 
remove a single level from unsafe reports. How many reports are now safe?
'''

safe_report_counter_2 = 0
for report in sanatized_input:
    if report_safety_check(report):
        safe_report_counter_2 += 1
    else:
        for x in range(len(report)):
            sub_report = report.copy()
            # Note to self: when using list.remove(item) the function removes all instances of that item in a list.
            # list.pop(index) on the other hand, removes the exact index
            sub_report.pop(x)
            if report_safety_check(sub_report):
                safe_report_counter_2 += 1
                break

print('Number of safe reports with the Problem Dampner: ', safe_report_counter_2)