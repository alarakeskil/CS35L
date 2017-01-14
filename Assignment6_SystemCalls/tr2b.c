#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void tr2b(char* from, char* to)
{
    // There are 256 ASCII chars, getchar() returns an int ASCII representation
    char ascii_chars[256];

    // Set every value in array to index
    int i;
    for(i = 0; i < 256; i++)
    {
        ascii_chars[i] = i;
    }

    // Replace every value in "from" with the corresponding one in "to"
    int j;
    for (j = 0; j < strlen(from); j++)
    {
        ascii_chars[from[j]] = to[j];
    }

    // Get input and putchar
    int c = getchar();
    while(c != EOF)
    {
        putchar(ascii_chars[c]);
        c = getchar();
    }
}

int main(int argc, char* argv[])
{
  // Check number of arguments
  if (argc != 3)
  {
    fprintf(stderr, "Incorrect number of arguments, requires 2 arguments.");
    exit(1);
  }

  // Check length of inputs
  char * from = argv[1];
  char * to = argv[2];

  if (strlen(from) != strlen(to))
  {
    fprintf(stderr, "Inputs must be the same length.");
    exit(1);
  }

  // Checks "from" for duplicates
  int i, j;
  for (i = 0; i < strlen(from); i++)
  {
    for (j = i + 1; j < strlen(from); j++)
    {
      if (from[i] == from[j])
      {
        fprintf(stderr, "Your from input should not contain any duplicate bytes");
        exit(1);
      }
    }
  }

  tr2b(argv[1], argv[2]);
}
