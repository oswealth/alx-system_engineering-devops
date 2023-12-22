#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
int infinite_while(void);

/**
 * main - main function
 *
 * Return: void function
 */
int main(void)
{
	int n = 0;

	while (n < 5)
	{
		if (fork() != 0)
			printf("Zombie process created, PID: %ld\n", (long)getpid());
		else
			return (0);
		n++;
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - indefinite while loop
 *
 * Return: void function
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
