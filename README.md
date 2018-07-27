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

**Precision** = 3/(3+1,299) = 0,0023 | **Recall** = 3/(4+3) = 0,42 | **F1 score** = 2 · (P·R)/(P+R) = 4,57 · 10<sup>-3</sup>


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
* Total number of TRACER results: 506,418
* Total number of TRACER results without duplicates: 502,877
* Reuses to find: 97
* TPs: 19
* FPs: 502,877-19 = 502,858
* FN: 78


**Precision** = 97/(97+502,858) = 0,000192 | **Recall** = 2/(78+19) = 0,02 | **F1 score** = 2 · (P·R)/(P+R) = 3,8 · 10<sup>-4</sup>


<!--## Example results

### False Negatives

<table>
    <thead>
        <tr>
            <th>Work</th>
            <th>Sentence</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ScG</td>
            <td>hinc etiam processit stoicorum opinio , qui dicebant cognitionem intellectus causari ex hoc quod <b>imagines</b> <b>corporum</b> nostris <b>mentibus imprimuntur</b> , sicut speculum quoddam , vel sicut <b>pagina</b> recipit <b>litteras</b> impressas , absque hoc quod aliquid agat : ut boetius narrat in v de consolatione</td>
            <td rowspan=2>in <code>.link</code>
             (overlap of 6) but not in <code>.score</code> file</td>
        </tr>
        <tr>
            <td>PC</td>
            <td>Quondam Porticus attulit obscuros nimium senes , qui sensus et <b>imagines</b> e <b>corporibus</b> extimis credant <b>mentibus imprimi</b> , ut quondam celeri stilo mos est aequore <b>paginae</b> , quae nullas habeat notas , pressas figere <b>litteras</b> .</td>
        </tr>
    </tbody>
</table>


<table>
    <thead>
        <tr>
            <th>Work</th>
            <th>Sentence</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ScG</td>
            <td>quia vero non omnis veritatis manifestandae modus est idem ; disciplinati autem hominis est tantum de unoquoque fidem capere tentare , quantum natura rei permittit , ut a philosopho , optime dictum boetius introducit , necesse est prius ostendere quis modus sit possibilis ad veritatem propositam menifestandam .</td>
            <td rowspan=2>in <code>.link</code>
             (overlap of 8) but not in <code>.score</code> file; missing syn relation (eruditus-disciplinatus); inconsistent lemmatisation (temptare-tentare)</td>
        </tr>
        <tr>
            <td>De Trinitate</td>
            <td>age igitur ingrediamur et unumquodque ut intellegi atque capi potest dispiciamus ; nam , sicut optime dictum uidetur , eruditi est hominis unum quodque ut ipsum est ita de eo fidem capere temptare .</td>
        </tr>
    </tbody>
</table>



### True Positives


**ScG (1.62.5)**: cum etiam deus sit primus intellectus et primum intelligibile , oportet quod veritas intellectus cuiuslibet eius veritate mensuretur : _si UNUMQUODQUE MENSURATUR PRIMO sui generis_ , ut philosophus tradit , in x metaphysicae .

(= translation) 

**Metaphysica (9.1.7-8.1052b24)**: Hinc autem et in aliis dicitur METRUM quo PRIMO UNUMQUODQUE cognoscitur . 

(= translation)

IT annotation: QL+QR | TRACER settings: | TRACER result: FN | Linking file: | Scoring file: | -->


## Copyright and Acknowledgements
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/) and was funded by the German Federal Ministry of Education and Research ([eTRAP](https://www.etrap.eu/), No. 01UG1409).
