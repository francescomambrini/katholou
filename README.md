# Katholou UD Treebanks of Ancient Greek

## Aims

*Katholou* collects a conversion of a series of treebanks of Ancient Greek into 
 the [Universal Dependency](https://universaldependencies.org/) format.
 
 The data are organized in subfolders, according to the source project they were 
 converted from (see Treebanks, below).
 
The conversion was made with using my [tb2ud](https://github.com/francescomambrini/tb2ud) 
routine. Please, report any issue using the [issue tracker](https://github.com/francescomambrini/katholou/issues). 
If you spot any conversion problem, you can use the special [ud conversion](https://github.com/francescomambrini/tb2ud) 
label to help me track them.

## Treebanks

At the moment we have conversions from the following projects:

* [Daphne](https://perseids-publications.github.io/daphne-trees/): my revised 
annotations on Sophocles (*Aj*., *El*., *OT*, *Ant*., *Tr*.), Aeschylus (*Ag*., 
*Eu*., *PV*).

* [Gorman Trees](https://perseids-publications.github.io/gorman-trees/): Vanessa 
Gorman's extensive annotation on a lot of prose authors and texts [[doi](https://doi.org/10.5281/zenodo.3596076)].

* [AGDT](https://perseusdl.github.io/treebank_data/): the Greek authors and texts, 
minus the one already included in Daphne or Gorman Trees; this means: *Il*., *Od*, 
Hesiod, *Hom. Hymn* 2. 

Coming soon:

* Hesiod from the [AGDT](https://perseusdl.github.io/treebank_data/).

* [Pedalion](https://perseids-publications.github.io/pedalion-trees/): annotations 
in the context of the [Pedalion](https://www.relicta.org/pedalion/glaux/) project, 
by Alek Keersmaekers, Ton van Hal et al.
 
 
## Name

*Katholou* (καθόλου), "on the whole, in general", is a word used especially by Aristotle 
to refer to the technical concept of "the universal", that which can be predicated 
of several individuals ([Peters 1967: 100-1](https://openlibrary.org/works/OL3486807W/Greek_philosophical_terms?edition=greekphilosophic0000pete)).

It seems like a good name for a project that:
1. adopts the [Universal Dependency](https://universaldependencies.org/) formalism;
2. aims to collect all the available Perseus-based treebanks.


## Attribution

The conversion is the work of F. Mambrini, though (at least at the moment) 
no manual post-processing or editing was performed on the output of the 
conversion scripts.

For the original annotations of the souce projects, see the `README` file in each 
of the subdirectories for more information and for attribution to the orignal authors.


## License

The data are distributed under a [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) 
license.

See the linked websites of th different projects for the licenses of the original data.
