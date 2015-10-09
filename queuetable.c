#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define N 100000

int d[2][N];
FILE * a;
char worker [10];
int b, c, i = 0;


int main(int argc, char *argv[])
{
	if (argc > 1)
	{
		// printf("%s", argv[1]);
		a = fopen(argv[1], "r");
		while (fscanf(a, "Came:%d, Started:%d, Finished:%d, Time:%d, service:%s\n",
						 &b, &b, &b, &c, worker) != EOF)
		{
			if ( !strcmp(worker, "able"))
				d[0][c] += 1;
			else 
				d[1][c] += 1;

			// printf("%s: %d\n", worker, c);
		}
		fclose(a);
		printf("Able Time:\n");
		for (i = 5; i < N; ++i)
		{
			if (d[0][i] != 0)
				printf("\t%d: %d\n", i - 5, d[0][i]);

		}
		printf("Baker Time:\n");
		for (i = 5; i < N; ++i)
		{
			if (d[1][i] != 0)
				printf("\t%d: %d\n", i - 10, d[1][i]);

		}
	}
	system("pause");
	return 0;
}

