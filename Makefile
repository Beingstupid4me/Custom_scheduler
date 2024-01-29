all: Q2.c counter_function.c 
	gcc -o counter_function counter_function.c
	gcc -o Q2 Q2.c
	> output.txt
	sudo taskset --cpu-list 1 "./Q2"
	python plotting.py
clean:
	rm counter_function
	rm Q2
	rm output.txt