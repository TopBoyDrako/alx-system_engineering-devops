#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    int i;
    pid_t child_pid;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();
        if (child_pid > 0)
        {
            printf("Zombie process created, PID: %d\n", child_pid);
            sleep(1); // Added a small delay to give the child processes a chance to become zombies
        }
        else
            exit(0);
    }

    infinite_while();

    return (0);
}

