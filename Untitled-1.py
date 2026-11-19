
def fifo_scheduling(processes):
    processes.sort(key=lambda x: x[1])

    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    print("PID\tAT\tBT\tCT\tWT\tTAT")

    for pid, arrival, burst in processes:
        if current_time < arrival:
            current_time = arrival

        completion = current_time + burst
        turnaround = completion - arrival
        waiting = turnaround - burst

        current_time = completion

        total_waiting_time += waiting
        total_turnaround_time += turnaround

        print(f"{pid}\t{arrival}\t{burst}\t"
              f"{completion}\t{waiting}\t{turnaround}")

    n = len(processes)

    print("\nAverage Waiting Time:",
          total_waiting_time / n)

    print("Average Turnaround Time:",
          total_turnaround_time / n)


# Process: (PID, Arrival Time, Burst Time)
processes = [
    ("P1", 0, 5),
    ("P2", 1, 3),
    ("P3", 2, 8),
    ("P4", 3, 6)
]

fifo_scheduling(processes)
