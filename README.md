# Text reuse in the *Summa contra Gentiles*
This research seeks to automatically detect text reuse (verbatim and paraphrase) between the *Summa contra Gentiles* of Thomas Aquinas and a number of other works. 

The detection software used is [TRACER](http://www.etrap.eu/research/tracer). The automatically-detected reuses are evaluated against the manually-annotated (explicit) quotations in the *Index Thomisticus*, which is used as a gold standard. 
The objective is to create an "Index fontium computatus" containing true positives, false positives as well as false negatives to better understand the limitations of retrieval methods and linguistic resources for Latin.

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## TreeTagger (Brandolini)

Overview of the tagging performance of the Brandolini TreeTagger Latin parameter file across the texts under study. Punctuation is excluded from the token count.


| Author              | Work                       | Tokens   | Unknowns (%)   |
| :---                | :---                       |    ---:  |           ---: |
| Thomas Aquinas      | Summa contra Gentiles      |  378,160 |	 4,396 (1.16%) |
| Aristoteles Latinus |	Metaphysica	               |   59,314 |  4,232 (7.13%) |
| Cicero              | De divinatione             |   28,744 |  2,690 (9.35%) |
| Boethius            | Philosophiae Consolationis |   24,924 |  2,279 (9.14%) |
| Apuleius            | De Deo Socratis			   |    4,633 |    410 (8.84%) |
| Boethius            | De Trinitate			   |    2,902 |     60 (2.06%) |


Average tagging accuracy: **93.72%**                                                     

                      




