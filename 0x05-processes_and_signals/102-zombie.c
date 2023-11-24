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
	for (int i = 0; i < 5; i++)
	{
		pid_t child_pid = fork();

		if (child_pid == -1)
		{
			perror("Fork failed");
			exit(EXIT_FAILURE);
		}

		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}

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
