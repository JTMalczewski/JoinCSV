# JoinCSV
## recruitment task
### Goal
Implement an executable program, which will read two csv files, join them using a specified column and then write the result to the standard output. Users should be able to specify the join type (inner, left or right).<br />
![cool spheres](https://c.tenor.com/lonETsK3tScAAAAC/pak-pak-merge.gif)

### Table of contents
- [Goal](#goal)
- [cool gif](#cool-spheres)
- [Technologies](#Technologies)
- [Launch](#Launch)
- [Attached databases](#Attached-databases)

### Technologies
Project is created with:
- NumPy 1.17.4
- Python 3.8.10

### Launch
To start the merging script run: <br /> `$ join.py file_path file_path column_name join_type` <br />
`file_path` - linuks path to csv datafile conform to the [rfc4180](https://datatracker.ietf.org/doc/html/rfc4180)
`column_name ` - choose the header of your column from data file for join operation
`join_type` - choose `inner`, `left` or `right`. By default join type is set to `inner`. This solution helps to spot significant lines and don't generate empty cells. To read more about join types, I recomend [metabase.com](https://www.metabase.com/learn/sql-questions/sql-join-types) article (basic SQL knowledge is needed).

### Attached databases
Test CSV files [source](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html):
- hw_200.csv `3.7 kB`
- hw_25000.csv `633,3 kB`
