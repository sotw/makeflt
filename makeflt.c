#include <stdio.h>
#define BLOCK_SIZE 512

void cp_stdin2stdout()
{
   char buffer[BLOCK_SIZE];
   for(;;){
      size_t bytes = fread(buffer, sizeof(char), BLOCK_SIZE, stdin);
      fwrite(buffer, sizeof(char), bytes, stdout);
      fflush(stdout);
      if( bytes < BLOCK_SIZE )
         if (feof(stdin))
            break;
   }
}

int main(int argc, const char *argv[])
{
   if( argc == 1 ){ // copy stdin to stdout
      cp_stdin2stdout();
   }
   else printf("Not implemented.\n");
   return 0;
}
