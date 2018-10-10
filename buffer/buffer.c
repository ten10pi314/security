#include <stdio.h>
#include <string.h>

void main(int argc, char *argv[])
{
	char buffer[5];
	if(argc<2) {
    	printf("Syntax: ./a.out user_input\n");
    	return;
	}
	strcpy(buffer, argv[1]);
	printf("Buffer: %s\n", buffer);
	return;
}
