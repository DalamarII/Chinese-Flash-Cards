Chinese-Flash-Cards
===================

Flash Cards to help you learn Chinese.

To use, provide a UTF-8 text file named "definitions.txt" in the same directory
as the python script. The program will read and parse that file to use as the
dictionary to test the user against.

The definitions.txt file format is still a work in progress. But here's a rough
grammmar:

<chinese phrase> - <word type> <definition>/[optional word type] <definition
2>/[optional word type] <definition 3>/...

In a nut shell, the '-' character separates the Chinese phrase from its
English definition. The '/' separates alternate definitions of the phrase. you
can have as many alternate definitions as you want.

It isn't enforced now. But you should really define at least one word type at
the beginning of the definition section.

A newline indicates a new dictionary entry.
