// CSE 374, HW 05
// TianYang Jin
// T9
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "trie.h"

#define MAX_LINE_SIZE 500

int main(int argc, char** argv) {
  struct TrieNode* root = NULL;
  root = buildTree(root, argv[1]);
  struct TrieNode* currNode = root;
  char line[MAX_LINE_SIZE];
  printf("Enter \"exit\" to quit.\n");
  printf("Enter Key Sequence (or \"#\" for the next word):\n> ");
  while (fgets(line, MAX_LINE_SIZE, stdin) != NULL
         && strncmp(line, "exit\n", MAX_LINE_SIZE) != 0) {
    if (strncmp(line, "#\n", MAX_LINE_SIZE) != 0) {
      currNode = root;
    }
    currNode = searchWord(currNode, line);
    if (currNode != NULL) {
      printf("\t\'%s\'\n", currNode->key);
    }
    printf("Enter Key Sequence (or \"#\" for the next word):\n> ");
  }
  currNode = NULL;
  freeNode(root);
}
