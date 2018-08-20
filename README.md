# name_generators

Generates names based on a set of corpuses and a pattern.




## Pattern Definitions

Each pattern consists of multiple space seperated pieces. Each piece has two parts, an
instruction section, and a tag. The instruction section informs what the tag represents,
and how it should be handled. The tag is an identifier of either a corpus, or a
reference to another pattern defined by the schema. The two sections of the piece are
delimited by a "#" mark. Everything to the right of the hash mark is considered part of
the tag. If a teg references a list, an item will be chose at random. If tag references
a string, the string will be given directly.


### Instruction Definitions

#### Execution Instructions
\* = Tag will reference plaintext of corpus of plaintext.
! = Tag references either pattern or corpus of patterns. 
$ = Tag itself is plaintext. 

#### Simple Instructions
^ = Capitalize Result
\+ = AllCaps Result
\- = lowercase result
