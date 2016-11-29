#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool win(){
	return true;
}

bool lose(){
	return false;
}


int main( int argc, char *argv[] )  {

	bool success = false;
	int value;
    if( argc < 2 ) {
        printf("Not enough args!\n");
        return -1;
    }

    value = atoi(argv[1]);
    if(value == 42){
    	success = win();
    }
    else{
    	success = lose();
    }

    return success;
}
