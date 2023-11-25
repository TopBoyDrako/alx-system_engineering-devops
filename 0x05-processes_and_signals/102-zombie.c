#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int infinite_while(void);

/**
* main - Creates 5 zombie processes and calls infinite_while
* Return: Always 0
*/

int main(void)
{
	int i = 0;
	pid_t pid;

	while (i < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %d\n", (int)pid);
		i++;
	}
	if (pid != 0)
		infinite_while();
	return (0);

}

/**
* infinite_while - Keeps the program running indefinitely
* Return: Always 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
