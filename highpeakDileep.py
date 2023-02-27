# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:59:03 2023

@author: dilee
"""

def get_max_profit_jobs(n, jobs):
    # Sort jobs by decreasing order of their profit
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Keep track of selected jobs and their end times
    selected_jobs = []
    end_times = []
    
    # Select jobs with highest profit that don't overlap with previous selections
    for job in jobs:
        start_time, end_time, profit = job
        overlaps = False
        for i in range(len(selected_jobs)):
            if start_time < end_times[i] and end_time > selected_jobs[i][0]:
                overlaps = True
                break
        if not overlaps:
            selected_jobs.append(job)
            end_times.append(end_time)
    
    # Calculate total earnings for Lokesh
    earnings = sum(job[2] for job in selected_jobs)
    
    # Calculate number of remaining jobs and their total earnings
    remaining_jobs = n - len(selected_jobs)
    remaining_earnings = sum(job[2] for job in jobs if job not in selected_jobs)
    
    return remaining_jobs, remaining_earnings
    
# Get number of jobs
n = int(input("Enter the number of Jobs: "))

# Get job details
jobs = []
for i in range(n):
    start_time = int(input("Enter start time for job {}: ".format(i+1)))
    end_time = int(input("Enter end time for job {}: ".format(i+1)))
    profit = int(input("Enter profit for job {}: ".format(i+1)))
    jobs.append((start_time, end_time, profit))

# Get max profit jobs and remaining jobs/earnings
remaining_jobs, remaining_earnings = get_max_profit_jobs(n, jobs)

# Output result
print("The number of tasks and earnings available for others")
print("Task:", remaining_jobs)
print("Earnings:", remaining_earnings)