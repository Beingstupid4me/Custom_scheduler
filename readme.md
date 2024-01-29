# Process Scheduling in C

This program demonstrates the use of different process scheduling policies in C. It creates three child processes, each with a different scheduling policy: `SCHED_OTHER`, `SCHED_RR`, and `SCHED_FIFO`. Each child process executes a counter function, and the time taken for each process to complete is recorded and written to a file.

## Code Structure

The code is structured as follows:

1. **Function Definitions**: The `time_used` function calculates the time difference between the start and end times of a process.

2. **Main Function**: The main function does the following:
   - Initializes variables for process IDs, scheduling parameters, and time tracking.
   - Creates three child processes in a loop. Each child process is assigned a different scheduling policy (`SCHED_OTHER`, `SCHED_RR`, or `SCHED_FIFO`) and executes the `counter_function`.
   - Waits for each child process to complete and records the end time.
   - Writes the time taken by each process to an output file.

## Usage

To run this program, just run the make command in terminal in this folder, it compiles it with a C compiler (like gcc), and then runs the resulting executable with the command `sudo taskset --cpu-list 1 "./Q2"`, this sets the affinity of the executable to 1, running the process on a single core. The output will be written to a file named `output.txt` in the same directory.

Please note that this program uses the `sched_setscheduler` function to set the scheduling policy of each child process, which may require root privileges depending on your system's configuration.

## Dependencies

This program requires the following headers:

- `stdio.h`
- `unistd.h`
- `sys/wait.h`
- `sched.h`
- `time.h`

## Output

The output of this program is a text file named `output.txt` that contains the time taken by each process under different scheduling policies.

Please replace `/home/amartya/Desktop/Codes/2022062_2022024/Q2/counter_function` with the actual path to your counter function, and `/home/amartya/Desktop/Codes/2022062_2022024/Q2/output.txt` with your desired output path.

So, as the priority of fifo and rr is 50 which is greater than 0 , they take lesser time than other
and among fifo and rr , fifo is taking lesser time because it is favored by the cpu when their is
same priority of both rr and fifo.


## Working

The program first creates three processes using loop, saving their start-time. It also sets their scheduling policy as required, and shows a success message if done successfully.

After that end-time of the processes is stored using a loop and `waitpid()` function call.

Then the program writes the total time used by the respective scheduling policies in the text file named `output.txt`

Finally, a python program is run to plot the time taken vs policy graph.

