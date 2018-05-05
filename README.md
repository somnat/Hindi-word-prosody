# Hindi-Word-Prosody-Hindi-G2P
- - Pronunciation lexicon or dictionary is one of the essential resource for building a Speech-to-Text(STT)  or Text-to-Speech (TTS). 
- - This library is intended for generating the phonemic sequence for a given Hindi graphemic input along with its word-level prosodic structure. 
- - The prosodic structure includes the syllable boundaries as well as the syllable weight.
- - The Heavy and Super heavy syllables are generally the stressed syllables. However, in some cases heavy syllables are not stressed. The above library includes all the rules to correctly capture the prosodic structure.
- - Hindi is a morphologically rich language. Therefore, all derived words and compound words delete schwa at morphological boundaries. Most of the work on the Hindi G2P either needs the morphological information. However, the current library is autonomus to those boundaries and generates correct form in most of the cases.

For example: कमला becomes 'kam.la: where "." is the syllable boundary and ' specifies the stressed syllable.

#### More details can be found in the following paper. 

https://cdn.iiit.ac.in/cdn/ltrc.iiit.ac.in/icon2017/proceedings/icon2017/pdf/W17-7502.pdf

If you are using the above software in your research work then cite  the above paper.

### How to run the library.

- - sudo pip install -r requirement.txt
- - python input.py

#### Step 2 will generate GUI and user can feed the words or files as input and the output will generated in GUI as well as in the form a text file.
