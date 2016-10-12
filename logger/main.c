#include <stdio.h>
#include "logger.h"
int main()
{
    int x = 199,i=0;
    char *s = "Bitter Truth";

    while(i<10)
    {
        LOG_PRINT("Hello World ");
        LOG_PRINT("Sebastian is back !!! %s %d",s,x++);
        i++;
    }
}
