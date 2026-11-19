# FIFO-First-In-First-Out-Scheduling-Algorithm

# FIFO (First In, First Out) Scheduling Algorithm

## Overview
This project implements and analyzes the **FIFO (First In, First Out)** scheduling algorithm, one of the simplest CPU scheduling algorithms used in operating systems.

FIFO follows the principle that the process arriving first in the ready queue is executed first. Processes are scheduled according to their arrival time, without preemption.

## Features
- Implementation of the FIFO scheduling algorithm.
- Process execution based on arrival time.
- Calculation of Waiting Time (WT).
- Calculation of Turnaround Time (TAT).
- Calculation of Completion Time (CT).
- Calculation of Average Waiting Time.
- Calculation of Average Turnaround Time.
- Visualization of process execution using a Gantt Chart.

## Scheduling Formulas

- **Completion Time (CT):** The time at which a process finishes execution.
- **Turnaround Time (TAT):** `TAT = CT - AT`
- **Waiting Time (WT):** `WT = TAT - BT`

Where:
- AT = Arrival Time
- BT = Burst Time

## Advantages
- Simple and easy to implement.
- Fair execution order based on arrival time.
- No starvation.

## Disadvantages
- Can cause the Convoy Effect.
- Short processes may wait behind longer processes.
- Average waiting time can be high.

## Technologies Used
- Programming Language: Python
- Algorithm: FIFO Scheduling

## Purpose
The purpose of this project is to understand the FIFO scheduling algorithm, evaluate its performance, and analyze its advantages and disadvantages in operating systems.
