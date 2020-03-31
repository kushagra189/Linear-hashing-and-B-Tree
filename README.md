# Part-1
## B-Plus-Tree

### Summary

**bplus**

* This file contains the operations like reading input file, reading parameters **M** and **B** and calling the below functions.

**create_tree**

* This file contains tree manipulations like **insertion**, **search of query**, **get keys**, **range query**.

**node_create**

* Creates nodes and takes care of splitting of the nodes.

# Part-2
## Linear Hashing

### Summary

* i - splitting round (determines hash function - h0 and h1 ... hi and h_i+1 )
* p - which bucket needs to be split next p_sequence = {0,1; 0,1,2,3; 0,1,2,3,4,5,6,7; 0,1,2,3,4...15; 0,..31; ...} Taken powers of 2.
* S - total number of records
* b -	initial hash function modulo 2

**Functions**

**insert**
* Insert new values in the hash table.

**hash_table_too_full**
* Check if density of hash table is more than 75% or not. If hash table too full then call **create_new_bucket** function.

**create_new_bucket**
* Creates new bucket when hash table has high density.
