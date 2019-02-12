# Hindi-Word-Prosody
- - Pronunciation lexicon is one of the essential resource for building a Speech-to-Text(STT)  or Text-to-Speech (TTS). 
- - This library is intended for generating the phonemic sequence for a given Hindi graphemic input along with its word-level prosodic structure. 
- - The prosodic structure includes the syllable boundaries as well as the syllable weight.
- - The Heavy and Super heavy syllables are generally the stressed syllables. However, in some cases heavy syllables are not stressed. The above library includes all the rules to correctly capture the prosodic structure.
- - Hindi is a morphologically rich language. Therefore, all derived words and compound words delete schwa at morphological boundaries.

For example: कमला becomes 'kam.la: where "." is the syllable boundary and ' specifies the stressed syllable.

#### More details can be found in the following paper. 




# Citations

Please cite Hindi-Word-Prosody in your publications if it helps your research.
The following is a [BibTeX](http://www.bibtex.org/) and plaintext reference for our
[Hindi-Word-Prosody](https://cdn.iiit.ac.in/cdn/ltrc.iiit.ac.in/icon2017/proceedings/icon2017/pdf/W17-7502.pdf).

```
@InProceedings{roy:2017:W17-75,
  author    = {Roy, Somnath},
  title     = {Deriving Word Prosody from Orthography in Hindi},
  booktitle = {Proceedings of the 14th International Conference on Natural Language Processing (ICON-2017)},
  month     = {December},
  year      = {2017},
  address   = {Kolkata, India},
  publisher = {NLP Association of India},
  pages     = {2--12},
  url       = {http://www.aclweb.org/anthology/W/W17/W17-7502}
}
```
### How to run the library.

- - sudo pip install -r requirement.txt
- - python input.py

#### Step 2 will generate GUI and user can feed the words or files as input and the output will generated in GUI as well as in the form a text file.
