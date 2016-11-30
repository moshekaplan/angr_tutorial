#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool is_magical(int number){
    number = number * 2;
    number += 10;
    for(int i=1; i<=6; i++){
        if(number % i != 0){
            return false;
        }
    }
    return true;
}


int main( int argc, char *argv[] )  {

    int value;
    if( argc < 2 ) {
        printf("Not enough args!\n");
        return -1;
    }

    value = atoi(argv[1]);

    if(is_magical(value)){
        printf("Your number is magical!\n");
    }
    else{
        printf("Not enough magic...\n");
    }

    return 0;
}
