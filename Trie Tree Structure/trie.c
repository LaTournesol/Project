// CSE 374, HW 05
// TianYang Jin
// Trie structure with the mothod to create a new trie, to add a word to
// an existing trie, to build a trie using a given file, and to search
// a given word in an existing trie.
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "trie.h"

// Initialize an empty TrieNode structure
struct TrieNode* createNewTrie() {
  struct TrieNode* trie = (struct TrieNode*)malloc(sizeof(struct TrieNode));
  trie->key = NULL;
  for (int i = 0; i < CHILDREN_SIZE; i++) {
    trie->children[i] = NULL;
  }
  return trie;
}

// Convert given character to its corresponding integer value
int charToInt(char c) {
  switch (c) {
  case '#': return 1;
  case 'a': case 'b': case 'c': return 2;
  case 'd': case 'e': case 'f': return 3;
  case 'g': case 'h': case 'i': return 4;
  case 'j': case 'k': case 'l': return 5;
  case 'm': case 'n': case 'o': return 6;
  case 'p': case 'q': case 'r': case's': return 7;
  case 't': case 'u': case 'v': return 8;
  case 'w': case 'x': case 'y': case 'z': return 9;
  default: return -1;
  }
}

// add a new word to the trie structure according to its integer sequence
struct TrieNode* addWord(struct TrieNode* root, char* word, int* intSequence) {
  int length = strlen(word) - 1;
  if (root == NULL) {
    root = createNewTrie();
  }
  struct TrieNode* currNode = root;
  // Walking down the trie using the int sequence
  for (int i = 0; i < length; i++) {
    int index = intSequence[i] - 1;
    if (currNode->children[index] == NULL) {
      currNode->children[index] = createNewTrie();
    }
    currNode = currNode->children[index];
  }
  // If word already exists, append to the # node
  while (currNode->key != NULL) {
    if (currNode->children[0] == NULL) {
      currNode->children[0] = createNewTrie();
    }
    currNode = currNode->children[0];
  }
  currNode->key = (char*)malloc(strlen(word));
  strncpy(currNode->key, word, length);
  currNode->key[length] = '\0';
  return root;
}

// Build a complete trie tree using a given dictionary file,
// give an error and exit if the given file cannot be opened.
struct TrieNode* buildTree(struct TrieNode* root, char* fileName) {
  FILE* fin = fopen(fileName, "r");
  if (fin == NULL) {
    fprintf(stderr, "Error: Fail to open file %s\n", fileName);
    exit(1);
  }
  char line[MAX_LINE_SIZE];
  while (fgets(line, MAX_LINE_SIZE, fin) != NULL) {
    int length = strlen(line) - 1;
    int* intSequence = (int*)malloc(length*sizeof(length));
    for (int i = 0; i < length; i++) {
      intSequence[i] = charToInt(line[i]);
    }
    root = addWord(root, line, intSequence);
    free(intSequence);
  }
  fclose(fin);
  return root;
}

// Treverse the trie tree starting at the startingNode according to the
// key sequence, return word if found, print out an appropriate error
// message to std if not.
struct TrieNode* searchWord(struct TrieNode* startingNode, char* keySequence) {
  if (startingNode != NULL) {
    struct TrieNode* currNode = startingNode;
    int length = strlen(keySequence) - 1;
    for (int i = 0; i < length; i++) {
      int index = keySequence[i] - '0';
      index--;
      if (keySequence[i] == '#') {
        index = 0;
      }
      if (currNode->children[index] == NULL) {
        if (keySequence[i] == '#') {
          errMsg1();
          return NULL;
        } else {
          errMsg2();
          return NULL;
        }
      } else {
        currNode = currNode->children[index];
      }
    }
    if (currNode->key == NULL) {
      if (keySequence[length - 1] == '#') {
        errMsg1();
        return NULL;
      } else {
        errMsg2();
        return NULL;
      }
    } else {
      return currNode;
    }
  } else {
    return NULL;
  }
}

// Free up all the allocted memory starting at a startingNode
void freeNode(struct TrieNode* startingNode) {
  if (startingNode == NULL) {
    return;
  }
  for (int i = 0; i < CHILDREN_SIZE; i++) {
    freeNode(startingNode->children[i]);
  }
  if (startingNode->key != NULL) {
    free(startingNode->key);
  }
  free(startingNode);
}

// Print an appropriate error message to stderr
void errMsg1() {
  fprintf(stderr, "\tThere are no more T9onyms.\n");
}

// Print an appropriate error message to stderr
void errMsg2() {
  fprintf(stderr, "\tNot found in current dictionary.\n");
}




