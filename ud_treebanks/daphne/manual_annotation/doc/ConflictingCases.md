# Conflicting annotations

This chapter discusses cases of possible overlap between different conflicting annotation. 
This refers to cases where we deal with constructions where two or more labels from the 
standard UD guidelines seem applicable or reasonable, or where inconsistences are actually 
attested in the existing UD annotations.

The cases are divided in the following sections:

* verbal constructions
* nominal constructions
* adverbials and particles

Within each group, they generally follow the alphabetic order of the first label involved.

## Verbal constructions

## Nominal constructions

### `apos` or `nmod`.

This is a frequently discussed topic! In general, we believe that there is a real difference between true appositions and attributive use of nouns. This is also the stance taken by the PDT guidelines, distinguishing between `ATR` and `_AP`.

The [French UD guidelines](https://universaldependencies.org/fr/dep/nmod-appos.html) introduce the `nmod:appos` for the attributive use, i.e. cases like:

```
Le journal Libération
l'affaire Dreyfus
...
```

`nmod:apos` should be used for phrases like:

```
θεὰ γαλυκῶπις Ἀθήνη
παῖ Νεοπτόλεμε
...
```
 



