#include<stdio.h>
#include<stdlib.h>
typedef union TEST{
    double x;
    long y;
}Test;
int main(int argc,char** argv){
    Test t;
    t.x = atof(argv[1]);
    printf("%ld %lx\n",t.y,t.y);
    return 0;
}