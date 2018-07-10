# Text reuse in the *Summa contra Gentiles*
This research seeks to automatically detect text reuse (verbatim and paraphrase) between the *Summa contra Gentiles* of Thomas Aquinas and a number of other works. 

The detection software used is [TRACER](http://www.etrap.eu/research/tracer). The automatically-detected reuses are evaluated against the manually-annotated quotations in the *Index Thomisticus*, which is used as a gold standard. 
The objective is to evaluate TRACER as an information retrieval tool for automatic text reuse detection and work towards the creation of an _Index fontium computatus_ containing true positives, false positives as well as false negatives to better understand the limitations of retrieval methods and linguistic resources for Latin.


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

## Summary of results and F1 scores

### Summa contra Gentiles vs. De Trinitate    

* Total number of sentences (_ScG_ and _De Trinitate_ combined): 19,560
* Total number of TRACER results: 10,708
* Total number of TRACER results without duplicates: 10,631
* Reuses to find: 4
* TPs: 3
* FPs: 10,631-4 = 10,627
* FN: 1

**Precision** = 3/(3+10,627) = 0,00028 | **Recall** = 3/(3+1) = 0,75 | **F1 score** = 2 · (P·R)/(P+R) = 5,59 · 10<sup>-4</sup>


### Summa contra Gentiles vs. Philosophiae Consolationis    

* Total number of sentences (_ScG_ and _Philosophiae Consolationis_ combined): 21,108
* Total number of TRACER results: 1,319
* Total number of TRACER results without duplicates: 1,306
* Reuses to find: 7
* TPs: 3
* FPs: 1,306-7 = 1,299
* FN: 4

**Precision** = 3/(3+1,299) = 0,0023 | **Recall** = 3/(4+3) = 0,42 | **F1 score** = 2 · (P·R)/(P+R) = 46 · 10<sup>-4</sup>


### Summa contra Gentiles vs. De Deo Socratis    

* Total number of sentences (_ScG_ and _De Deo Socratis_ combined): 19,600
* Total number of TRACER results: 167,075
* Total number of TRACER results without duplicates: 155,848
* Reuses to find: 2
* TPs: 2
* FPs: 155,848-2 = 155,846
* FN: 0

**Precision** = 2/(2+155,846) = 0,0000128 | **Recall** = 2/(0+2) = 1 | **F1 score** = 2 · (P·R)/(P+R) = 2,57 · 10<sup>-5</sup>


### Summa contra Gentiles vs. De Divinatione

* Total number of sentences (_ScG_ and _De Divinatione_ combined): 20,820
* Total number of TRACER results: 1,585,719
* Total number of TRACER results without duplicates: 
* Reuses to find: 1

No results. 


### Summa contra Gentiles vs. Metaphysica

* Total number of sentences (_ScG_ and _De Divinatione_ combined): 22,550
* Total number of TRACER results: 
* Total number of TRACER results without duplicates:
* Reuses to find: 

## Copyright and Acknowledgements
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/) and was funded by the German Federal Ministry of Education and Research ([eTRAP](https://www.etrap.eu/), No. 01UG1409).
