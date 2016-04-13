// CSE 374, HW 05
// TianYang Jin
// header file of the trie structure
#ifndef TRIE_H
#define TRIE_H

#define CHILDREN_SIZE 9
#define MAX_LINE_SIZE 500

// Structure of TrieNode, containing a string and a number of
// child nodes
struct TrieNode {
  char * key;
  struct TrieNode*  children[CHILDREN_SIZE];
};
// Initialize an empty TrieNode structure
struct TrieNode* createNewTrie();
// Convert given character to its corresponding integer value
int charToInt(char c);
// add a new word to the trie structure according to its integer sequence
struct TrieNode* addWord(struct TrieNode* root, char* word, int* intSequence);
// Build a complete trie tree using a given dictionary file,
// give an error and exit if the given file cannot be opened.
struct TrieNode* buildTree(struct TrieNode* root, char* fileName);
// Treverse the trie tree starting at the startingNode according to the
// key sequence, return word if found, print out an appropriate error
// message to std if not.
struct TrieNode* searchWord(struct TrieNode* startingNode, char* keySequence);
// Free up all the allocted memory starting at a startingNode
void freeNode(struct TrieNode* startingNode);
// Print an appropriate error message to stderr
void errMsg1();
// Print an appropriate error message to stderr
void errMsg2();
#endif
