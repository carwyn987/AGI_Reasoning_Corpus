# AGI_REASONING_CORPUS

An AGI testbed, primarily aimed at testing abstraction and generalization ability, without the limitations of the ARC-AGI corpus.

# Datasets

## ARC-AGI Dataset

The Abstraction and Reasoning Corpus for AGI (ARC-AGI) is both a dataset and a challenge. The dataset consists of input-output pairs, with each element consisting of a grid with various colors, or equivalently, integer encodings. The goal of the challenge is to transform an input to an output, and the transformations often involve straightforward and/or human intuitive mappings, dealing with symmetry, color remapping, etc. Transformations may also change the size of the grids, however, they are always square. When given a challenge, a couple reference mappings (inputs and outputs) are provided, as well as the "test" input. The user or machine attempting to solve first attempts to determine the rule from the input-output pairs, and then applies said rule to the test input to determine the submitted answer. In the dataset, there may be variable numbers of input-output reference pairs. Each challenge is given in json format.

Source: [https://arcprize.org/](arcprize.org)

## RAVEN Dataset

Source: []()